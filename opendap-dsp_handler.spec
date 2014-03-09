Summary:	DSP data handler for the OPeNDAP data server
Summary(pl.UTF-8):	Moduł obsługujący dane DSP dla serwera danych OPeNDAP
Name:		opendap-dsp_handler
Version:	3.7.0
Release:	0.1
License:	LGPL v2.1+
Group:		Daemons
Source0:	http://www.opendap.org/pub/source/dsp_handler-%{version}.tar.gz
# Source0-md5:	5ad9e0f387dd4494785b10d15b8f51d0
URL:		http://opendap.org/
#BuildRequires:	DSP software (formerly at ftp://sapodilla.rsmas.miami.edu/pub/dsp/)
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	libdap-devel >= 3.7.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	pkgconfig
Requires:	libdap >= 3.7.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the DSP data handler for OPeNDAP data server.

%description -l pl.UTF-8
Ten pakiet zawiera moduł obsługi danych DSP dla serwera danych
OPeNDAP.

%prep
%setup -q -n dsp_handler-%{version}

%build
# rebuild autotools for -as-needed to work
%{__libtoolize}
%{__aclocal} -I conf
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYRIGHT ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/dap_dsp_handler
