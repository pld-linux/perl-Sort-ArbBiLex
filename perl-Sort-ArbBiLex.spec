%include	/usr/lib/rpm/macros.perl
%define	pdir	Sort
%define	pnam	ArbBiLex
Summary:	Sort-ArbBiLex perl module
Summary(pl):	Modu³ perla Sort-ArbBiLex
Name:		perl-Sort-ArbBiLex
Version:	3.32
Release:	5
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sort-ArbBiLex - makes sort functions for arbitrary sort orders.

%description -l pl
Sort-ArbBiLex - tworzy funkcje sortuj±ce dla dowolnej kolejno¶ci
sortowania.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf ChangeLog README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Sort/ArbBiLex.pm
%{_mandir}/man3/*
