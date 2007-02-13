#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	X500
%define	pnam	DN
Summary:	X500::DN - handle X.500 DNs (Distinguished Names), parse and format them
Summary(pl.UTF-8):	X500::DN - obsługa DN (Distinguished Names) X.500, analiza i formatowanie ich
Name:		perl-X500-DN
Version:	0.28
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a600373d73ab59eb6e28d26f14cb8df1
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module handles X.500 DNs (Distinguished Names). Currently, it
parses DN strings formatted according to RFC 2253 syntax into an
internal format and produces RFC 2253 formatted string from it.

%description -l pl.UTF-8
Ten moduł obsługuje DN (Distinguished Names) X.500. Aktualnie
analizuje łańcuchy DN sformatowane zgodnie ze składnią RFC 2253 na
wewnętrzny format i tworzy z niego łańcuchy sformatowane zgodnie z
RFC 2253.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/X500/*.pm
%{_mandir}/man3/*
