#
#
Summary:	.NET bindings for GTK+ API not included in GTK#
Summary(pl.UTF-8):	Wiązania GTK+ API nie włączonego do GTK# dla .NET
Name:		dotnet-gtk-sharp-beans
Version:	2.14.0
Release:	2
License:	LGPL v2.1
Group:		Libraries
Source0:	gtk-sharp-beans-%{version}.tar.gz
# Source0-md5:	7ad55e25b0338927dcb501445f847450
URL:		http://github.com/mono/gtk-sharp-beans/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dotnet-gio-sharp-devel
BuildRequires:	dotnet-gtk-sharp2-devel >= 2.12.0
BuildRequires:	gtk+2-devel >= 2:2.16.0
BuildRequires:	mono-csharp
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(monoautodeps)
Requires:	gtk+2 >= 2:2.16.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides bindings for .NET to GTK+ API not included in
GTK#.

%description -l pl.UTF-8
Pakiet ten dostarcza wiązania dla .NET do GTK+ API nie włączonego do
GTK#.

%package devel
Summary:	GTK#Beans development files
Summary(pl.UTF-8):	Pliki programistyczne GTK#Beans
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	dotnet-gtk-sharp2-devel >= 2.12.0

%description devel
GTK#Beans development files.

%description devel -l pl.UTF-8
Pliki programistyczne GTK#Beans.

%prep
%setup -q -n mono-gtk-sharp-beans-19023b6/

%build
mkdir config
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_prefix}/lib/gtk-sharp-beans

%files devel
%defattr(644,root,root,755)
%{_pkgconfigdir}/gtk-sharp-beans-2.0.pc
