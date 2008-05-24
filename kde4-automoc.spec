%define		orgname	automoc
Summary:	automoc
Summary(pl.UTF-8):	automoc
Name:		kde4-automoc
Version:	0.0.811226
Release:	0.1
License:	GPL v2
Group:		X11/Applications
Source0:	%{orgname}-%{version}.tar.bz2
# Source0-md5:	ad6209138f9c80438c464c8922bd80ec
Patch0:		%{name}-lib64.patch
BuildRequires:	cmake
BuildRequires:	rpmbuild(macros) >= 1.293
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
automoc.

%description -l pl.UTF-8
automoc.

%prep
%setup -q -n %{orgname}
%if "%{_lib}" == "lib64"
%patch0 -p0
%endif

%build
install -d build
cd build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DQT_QMAKE_EXECUTABLE=%{_bindir}/qmake-qt4 \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/automoc4
%dir %{_libdir}/automoc4
%{_libdir}/automoc4/Automoc4Config.cmake
%{_libdir}/automoc4/automoc4.files.in
