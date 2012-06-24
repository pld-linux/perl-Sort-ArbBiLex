%include	/usr/lib/rpm/macros.perl
%define	pdir	Sort
%define	pnam	ArbBiLex
Summary:	Sort::ArbBiLex perl module
Summary(pl):	Modu� perla Sort::ArbBiLex
Name:		perl-Sort-ArbBiLex
Version:	3.4
Release:	2
Epoch:		1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sort::ArbBiLex - makes sort functions for arbitrary sort orders.

%description -l pl
Sort::ArbBiLex - modu� tworz�cy funkcje sortuj�ce dla dowolnej
kolejno�ci sortowania.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_vendorlib}/Sort/ArbBiLex.pm
%{_mandir}/man3/*
