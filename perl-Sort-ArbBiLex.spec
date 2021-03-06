#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Sort
%define		pnam	ArbBiLex
Summary:	Sort::ArbBiLex perl module
Summary(pl.UTF-8):	Moduł perla Sort::ArbBiLex
Name:		perl-Sort-ArbBiLex
Version:	4.01
Release:	2
Epoch:		1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9996bae43334fc9bb318e99f2d11cfc5
URL:		http://search.cpan.org/dist/Sort-ArbBiLex/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sort::ArbBiLex - makes sort functions for arbitrary sort orders.

%description -l pl.UTF-8
Sort::ArbBiLex - moduł tworzący funkcje sortujące dla dowolnej
kolejności sortowania.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests: %{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_vendorlib}/Sort/ArbBiLex.pm
%{_mandir}/man3/*
