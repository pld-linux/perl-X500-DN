#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	X500
%define	pnam	DN
Summary:	X500::DN - handle X.500 DNs (Distinguished Names), parse and format them
#Summary(pl):	
Name:		perl-X500-DN
Version:	0.28
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/X500/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a600373d73ab59eb6e28d26f14cb8df1
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module handles X.500 DNs (Distinguished Names).
Currently, it parses DN strings formatted according to RFC 2253 syntax into an
internal format and produces RFC 2253 formatted string from it.

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
