%include	/usr/lib/rpm/macros.perl
Summary:	Sort-ArbBiLex perl module
Summary(pl):	Modu� perla Sort-ArbBiLex
Name:		perl-Sort-ArbBiLex
Version:	3.1
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Sort/Sort-ArbBiLex-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Sort-ArbBiLex - makes sort functions for arbitrary sort orders.

%description -l pl
Sort-ArbBiLex - tworzy funkcje sortuj�ce dla dowolnej kolejno�ci sortowania.

%prep
%setup -q -n Sort-ArbBiLex-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Sort/ArbBiLex
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        ChangeLog README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {ChangeLog,README}.gz

%{perl_sitelib}/Sort/ArbBiLex.pm
%{perl_sitearch}/auto/Sort/ArbBiLex

%{_mandir}/man3/*
