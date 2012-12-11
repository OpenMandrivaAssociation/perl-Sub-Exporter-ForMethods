%define upstream_name    Sub-Exporter-ForMethods
%define upstream_version 0.100050

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Helper routines for using Sub::Exporter to build methods
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Sub/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Sub::Exporter)
BuildRequires:	perl(Sub::Name)
BuildArch:	noarch

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
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 0.100.50-2mdv2011.0
+ Revision: 654300
- rebuild for updated spec-helper

* Wed Jan 06 2010 Jérôme Quelin <jquelin@mandriva.org> 0.100.50-1mdv2011.0
+ Revision: 486606
- update to 0.100050

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.91.970-1mdv2010.1
+ Revision: 461734
- import perl-Sub-Exporter-ForMethods


* Fri Nov 06 2009 cpan2dist 0.091970-1mdv
- initial mdv release, generated with cpan2dist
