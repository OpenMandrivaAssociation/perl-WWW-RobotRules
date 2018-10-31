%define modname	WWW-RobotRules
%define modver 6.02

Summary:	Parse /robots.txt file
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	10
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/WWW/WWW-RobotRules-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires:	perl(AnyDBM_File)
BuildRequires:	perl(Fcntl)
BuildRequires:	perl(URI)

%description
This module parses _/robots.txt_ files as specified in "A Standard for
Robot Exclusion", at <http://www.robotstxt.org/wc/norobots.html> Webmasters
can use the _/robots.txt_ file to forbid conforming robots from accessing
parts of their web site.

The parsed files are kept in a WWW::RobotRules object, and this object
provides methods to check if access to a given URL is prohibited. The same
WWW::RobotRules object can be used for one or more parsed _/robots.txt_
files on any number of hosts.

The following methods are provided:

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{perl_vendorlib}/*
%{_mandir}/man3/*
