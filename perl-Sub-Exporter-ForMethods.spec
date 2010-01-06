%define upstream_name    Sub-Exporter-ForMethods
%define upstream_version 0.100050

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Helper routines for using Sub::Exporter to build methods
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Sub/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Sub::Exporter)
BuildRequires: perl(Sub::Name)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
The synopsis section, above, looks almost indistinguishable from any other
use of Sub::Exporter, apart from the use of 'method_installer'. It is
nearly indistinguishable in behavior, too. The only change is that
subroutines exported from Method::Builder into named slots in
Vehicle::Autobot will be wrapped in a subroutine called
'Vehicle::Autobot::transform'. This will insert a named frame into stack
traces to aid in debugging.

More importantly (for the author, anyway), they will not be removed by
namespace::autoclean. This makes the following code work:

  package MyLibrary;

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc LICENSE README
%{_mandir}/man3/*
%perl_vendorlib/*


