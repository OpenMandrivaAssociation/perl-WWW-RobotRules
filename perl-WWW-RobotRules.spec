%define upstream_name WWW-RobotRules
%define upstream_version 6.01

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Parse /robots.txt file
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/WWW/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(AnyDBM_File)
BuildRequires:	perl(Fcntl)
BuildRequires:	perl(URI)
BuildArch:	noarch

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
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 6.10.0-3mdv2012.0
+ Revision: 765807
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 6.10.0-2
+ Revision: 764331
- rebuilt for perl-5.14.x

* Tue May 03 2011 Guillaume Rousse <guillomovitch@mandriva.org> 6.10.0-1
+ Revision: 664982
- import perl-WWW-RobotRules

