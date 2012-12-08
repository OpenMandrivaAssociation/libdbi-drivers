Summary:	Database drivers for libdbi
Name:		libdbi-drivers
Version:	0.8.3
Release:	14
License:	LGPL
Group:		System/Libraries
URL:		http://libdbi-drivers.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/libdbi-drivers/%{name}-%{version}-1.tar.gz
BuildRequires:	libtool
BuildRequires:	autoconf
BuildRequires:	mysql-devel
BuildRequires:	postgresql-devel
BuildRequires:	sqlite-devel
BuildRequires:	sqlite3-devel
BuildRequires:	freetds-devel >= 0.62.4
BuildRequires:	dbi-devel >= 0.8.3
BuildRequires:	openjade
BuildRequires:	docbook-style-dsssl
BuildRequires:	docbook-dtd41-sgml

%description
libdbi implements a database-independent abstraction layer in C, similar to the
DBI/DBD layer in Perl. Writing one generic set of code, programmers can
leverage the power of multiple databases and multiple simultaneous database
connections by using this framework.

%package	dbd-mysql
Summary:	MySQL driver for libdbi
Group:		System/Libraries

%description	dbd-mysql
libdbi implements a database-independent abstraction layer in C, similar to the
DBI/DBD layer in Perl. Writing one generic set of code, programmers can
leverage the power of multiple databases and multiple simultaneous database
connections by using this framework.

This driver provides connectivity to MySQL database servers through the libdbi
database independent abstraction layer. Switching a program's driver does not
require recompilation or rewriting source code.

%package	dbd-pgsql
Summary:	PostgreSQL driver for libdbi
Group:		System/Libraries

%description	dbd-pgsql
libdbi implements a database-independent abstraction layer in C, similar to the
DBI/DBD layer in Perl. Writing one generic set of code, programmers can
leverage the power of multiple databases and multiple simultaneous database
connections by using this framework.

This driver provides connectivity to PostgreSQL database servers through the
libdbi database independent abstraction layer. Switching a program's driver
does not require recompilation or rewriting source code.

%package	dbd-sqlite
Summary:	SQLite driver for libdbi
Group:		System/Libraries

%description	dbd-sqlite
libdbi implements a database-independent abstraction layer in C, similar to the
DBI/DBD layer in Perl. Writing one generic set of code, programmers can
leverage the power of multiple databases and multiple simultaneous database
connections by using this framework.

This driver provides connectivity to SQLite database servers through the libdbi
database independent abstraction layer. Switching a program's driver does not
require recompilation or rewriting source code.

%package	dbd-sqlite3
Summary:	SQLite3 driver for libdbi
Group:		System/Libraries

%description	dbd-sqlite3
libdbi implements a database-independent abstraction layer in C, similar to the
DBI/DBD layer in Perl. Writing one generic set of code, programmers can
leverage the power of multiple databases and multiple simultaneous database
connections by using this framework.

This driver provides connectivity to SQLite3 database servers through the
libdbi database independent abstraction layer. Switching a program's driver
does not require recompilation or rewriting source code.

%package	dbd-freetds
Summary:	MSSQL (FreeTDS) driver for libdbi
Group:		System/Libraries

%description	dbd-freetds
libdbi implements a database-independent abstraction layer in C, similar to the
DBI/DBD layer in Perl. Writing one generic set of code, programmers can
leverage the power of multiple databases and multiple simultaneous database
connections by using this framework.

This driver provides connectivity to MSSQL database servers through the libdbi
database independent abstraction layer. Switching a program's driver does not
require recompilation or rewriting source code.

%package	devel
Summary:	Static library and header files for the %{name} library drivers
Group:		Development/C
Provides:	%{name}-drivers-devel
Requires:	dbi-devel >= 0.8.2

%description	devel
libdbi implements a database-independent abstraction layer in C, similar to the
DBI/DBD layer in Perl. Writing one generic set of code, programmers can
leverage the power of multiple databases and multiple simultaneous database
connections by using this framework.

This package contains the static libraries and header files.

%prep
%setup -q -n %{name}-%{version}-1

# fix dir perms
find -type d | xargs chmod 755

# lib64 fix
perl -pi -e "s|/lib\b|/%{_lib}|g" acinclude.m4

%build
sh autogen.sh

%configure2_5x \
    --enable-shared \
    --enable-static \
    --with-mysql \
    --with-pgsql \
    --with-sqlite \
    --with-sqlite3 \
    --with-freetds \
    --with-freetds-incdir=%{_includedir} \
    --with-freetds-libdir=%{_libdir} \
    --with-dbi-incdir=%{_includedir}/dbi \
    --with-dbi-libdir=%{_libdir}

%make

%install
%makeinstall_std

# install development headers
install -d %{buildroot}%{_includedir}/dbi
install -m0644 drivers/mysql/dbd_mysql.h %{buildroot}%{_includedir}/dbi/
install -m0644 drivers/pgsql/dbd_pgsql.h %{buildroot}%{_includedir}/dbi/
install -m0644 drivers/sqlite/dbd_sqlite.h %{buildroot}%{_includedir}/dbi/
install -m0644 drivers/sqlite3/dbd_sqlite3.h %{buildroot}%{_includedir}/dbi/
install -m0644 drivers/freetds/dbd_freetds.h %{buildroot}%{_includedir}/dbi/

# fix some docs
cp drivers/mysql/TODO TODO.mysql
cp drivers/pgsql/TODO TODO.pgsql
cp drivers/sqlite/TODO TODO.sqlite
cp drivers/sqlite3/TODO TODO.sqlite3

# cleanup
rm -rf %{buildroot}%{_docdir}/%{name}*

%files dbd-mysql
%doc drivers/mysql/README
%doc drivers/mysql/AUTHORS
%doc drivers/mysql/dbd_mysql
%doc drivers/mysql/dbd_mysql.pdf
%{_libdir}/dbd/libdbdmysql.so

%files dbd-pgsql
%doc drivers/pgsql/README
%doc drivers/pgsql/AUTHORS
%doc drivers/pgsql/dbd_pgsql
%doc drivers/pgsql/dbd_pgsql.pdf
%{_libdir}/dbd/libdbdpgsql.so

%files dbd-sqlite
%doc drivers/sqlite/README
%doc drivers/sqlite/AUTHORS
%doc drivers/sqlite/dbd_sqlite
%doc drivers/sqlite/dbd_sqlite.pdf
%{_libdir}/dbd/libdbdsqlite.so

%files dbd-sqlite3
%doc drivers/sqlite3/AUTHORS
%doc drivers/sqlite3/README
%doc drivers/sqlite3/AUTHORS
%doc drivers/sqlite3/dbd_sqlite3
%doc drivers/sqlite3/dbd_sqlite3.pdf
%{_libdir}/dbd/libdbdsqlite3.so

%files dbd-freetds
%doc drivers/freetds/README
%{_libdir}/dbd/libdbdfreetds.so

%files devel
%doc AUTHORS ChangeLog INSTALL README TODO*
%{_libdir}/dbd/*.a
%{_includedir}/dbi/*.h


%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 0.8.3-11mdv2011.0
+ Revision: 662357
- mass rebuild

* Thu Mar 17 2011 Oden Eriksson <oeriksson@mandriva.com> 0.8.3-10
+ Revision: 645748
- relink against libmysqlclient.so.18

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.8.3-9mdv2011.0
+ Revision: 609652
- rebuilt against new libdbi

* Thu Nov 25 2010 Oden Eriksson <oeriksson@mandriva.com> 0.8.3-8mdv2011.0
+ Revision: 601040
- rebuild

* Wed Feb 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0.8.3-7mdv2010.1
+ Revision: 507030
- rebuild

* Sat Sep 12 2009 Thierry Vignaud <tv@mandriva.org> 0.8.3-6mdv2010.0
+ Revision: 438546
- rebuild

* Sat Dec 06 2008 Oden Eriksson <oeriksson@mandriva.com> 0.8.3-5mdv2009.1
+ Revision: 311244
- rebuilt against mysql-5.1.30 libs

* Fri Jul 11 2008 Oden Eriksson <oeriksson@mandriva.com> 0.8.3-4mdv2009.0
+ Revision: 233768
- rebuild

* Mon Jun 16 2008 Anssi Hannula <anssi@mandriva.org> 0.8.3-3mdv2009.0
+ Revision: 219475
- build with main freetds, it has equal functionality now

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 0.8.3-2mdv2008.1
+ Revision: 178294
- bump release
- 0.8.3-1

* Sun Feb 17 2008 Oden Eriksson <oeriksson@mandriva.com> 0.8.3-1mdv2008.1
+ Revision: 169620
- 0.8.3

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Sep 06 2007 Oden Eriksson <oeriksson@mandriva.com> 0.8.2-1mdv2008.0
+ Revision: 81075
- 0.8.2-1


* Fri Jan 19 2007 Oden Eriksson <oeriksson@mandriva.com> 0.8.1-2mdv2007.0
+ Revision: 110697
- rebuilt against new postgresql libs

* Sat Dec 09 2006 Oden Eriksson <oeriksson@mandriva.com> 0.8.1-1mdv2007.1
+ Revision: 94098
- fix doc inclusion
- added the sqlite3 driver
- Import libdbi-drivers

* Wed Aug 02 2006 Oden Eriksson <oeriksson@mandriva.com> 0.8.1-1mdk
- 0.8.1
- added the freetds backend

* Sun Oct 30 2005 Oden Eriksson <oeriksson@mandriva.com> 0.8.0-2mdk
- rebuilt against MySQL-5.0.15

* Fri Sep 02 2005 Oden Eriksson <oeriksson@mandriva.com> 0.8.0-1mdk
- 0.8.0

* Wed May 11 2005 Oden Eriksson <oeriksson@mandriva.com> 0.7.1-2mdk
- lib64 fixes (P0)

* Fri Jun 18 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.7.1-1mdk
- 0.7.1

