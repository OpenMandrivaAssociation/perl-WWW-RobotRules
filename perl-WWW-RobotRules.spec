%define upstream_name    WWW-RobotRules
%define upstream_version 6.01

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 3

Summary:    Parse /robots.txt file
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/WWW/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(AnyDBM_File)
BuildRequires: perl(Fcntl)
BuildRequires: perl(URI)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*


