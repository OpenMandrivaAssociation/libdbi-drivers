%define	major 0
%define libname	%mklibname dbi %{major}

Summary:	Database drivers for libdbi
Name:		libdbi-drivers
Version:	0.8.1
Release:	%mkrel 2
License:	LGPL
Group:		System/Libraries
URL:		http://libdbi-drivers.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/libdbi-drivers/%{name}-%{version}a.tar.bz2
Patch0:		libdbi-drivers-0.8.1-freetds_mssql.diff
BuildRequires:	libtool
BuildRequires:	autoconf2.5
BuildRequires:	MySQL-devel
BuildRequires:	postgresql-devel
BuildRequires:	sqlite-devel
BuildRequires:	sqlite3-devel
BuildRequires:	freetds_mssql-devel >= 0.62.4
BuildRequires:	libdbi-devel >= 0.8.1
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
libdbi implements a database-independent abstraction layer in C,
similar to the DBI/DBD layer in Perl. Writing one generic set of
code, programmers can leverage the power of multiple databases and
multiple simultaneous database connections by using this
framework.

%package	dbd-mysql
Summary:	MySQL driver for libdbi
Group:		System/Libraries

%description	dbd-mysql
This driver provides connectivity to MySQL database servers through the
libdbi database independent abstraction layer. Switching a program's driver
does not require recompilation or rewriting source code.

%package	dbd-pgsql
Summary:	PostgreSQL driver for libdbi
Group:		System/Libraries

%description	dbd-pgsql
This driver provides connectivity to PostgreSQL database servers through the
libdbi database independent abstraction layer. Switching a program's driver
does not require recompilation or rewriting source code.

%package	dbd-sqlite
Summary:	SQLite driver for libdbi
Group:		System/Libraries

%description	dbd-sqlite
This driver provides connectivity to SQLite database servers through the
libdbi database independent abstraction layer. Switching a program's driver
does not require recompilation or rewriting source code.

%package	dbd-sqlite3
Summary:	SQLite3 driver for libdbi
Group:		System/Libraries

%description	dbd-sqlite3
This driver provides connectivity to SQLite3 database servers through the
libdbi database independent abstraction layer. Switching a program's driver
does not require recompilation or rewriting source code.

%package	dbd-freetds
Summary:	MSSQL (FreeTDS) driver for libdbi
Group:		System/Libraries

%description	dbd-freetds
This driver provides connectivity to MSSQL database servers through the
libdbi database independent abstraction layer. Switching a program's driver
does not require recompilation or rewriting source code.

%package	devel
Summary:	Static library and header files for the %{name} library drivers
Group:		Development/C
Provides:	%{name}-drivers-devel
Requires:	libdbi-devel >= 0.8.1

%description	devel
libdbi implements a database-independent abstraction layer in C,
similar to the DBI/DBD layer in Perl. Writing one generic set of
code, programmers can leverage the power of multiple databases and
multiple simultaneous database connections by using this
framework.

%prep

%setup -q -n %{name}-%{version}
%patch0 -p0

# fix dir perms
find -type d | xargs chmod 755

# lib64 fix
perl -pi -e "s|/lib\b|/%{_lib}|g" acinclude.m4

%build
sh autogen.sh

%configure2_5x \
    --with-mysql \
    --with-pgsql \
    --with-sqlite \
    --with-sqlite3 \
    --with-freetds \
    --with-freetds-incdir=%{_includedir}/freetds_mssql \
    --with-freetds-libdir=%{_libdir}

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

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

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files dbd-mysql
%defattr(-,root,root)
%doc drivers/mysql/README
%doc drivers/mysql/AUTHORS
%doc drivers/mysql/dbd_mysql
%doc drivers/mysql/dbd_mysql.pdf
%{_libdir}/dbd/libdbdmysql.so

%files dbd-pgsql
%defattr(-,root,root)
%doc drivers/pgsql/README
%doc drivers/pgsql/AUTHORS
%doc drivers/pgsql/dbd_pgsql
%doc drivers/pgsql/dbd_pgsql.pdf
%{_libdir}/dbd/libdbdpgsql.so

%files dbd-sqlite
%defattr(-,root,root)
%doc drivers/sqlite/README
%doc drivers/sqlite/AUTHORS
%doc drivers/sqlite/dbd_sqlite
%doc drivers/sqlite/dbd_sqlite.pdf
%{_libdir}/dbd/libdbdsqlite.so

%files dbd-sqlite3
%defattr(-,root,root)
%doc drivers/sqlite3/AUTHORS
%doc drivers/sqlite3/README
%doc drivers/sqlite3/AUTHORS
%doc drivers/sqlite3/dbd_sqlite3
%doc drivers/sqlite3/dbd_sqlite3.pdf
%{_libdir}/dbd/libdbdsqlite3.so

%files dbd-freetds
%defattr(-,root,root)
%doc drivers/freetds/README
%{_libdir}/dbd/libdbdfreetds.so

%files devel
%defattr(-,root,root)
%doc AUTHORS ChangeLog INSTALL README TODO*
%{_libdir}/dbd/*.a
%{_libdir}/dbd/*.la
%{_includedir}/dbi/*.h


