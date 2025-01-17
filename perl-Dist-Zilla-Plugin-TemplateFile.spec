%define upstream_name    Dist-Zilla-Plugin-TemplateFile
%define upstream_version 0.01

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Use files as templates to build a distribution
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Dist/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Dist::Zilla::Role::FileMunger)
BuildRequires:	perl(Dist::Zilla::Role::TextTemplate)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Moose::Autobox)
BuildRequires:	perl(namespace::autoclean)
BuildArch:	noarch

%description
Utilize the Text::Template manpage to turn certain files into templates.
Each template has available to it the '$dist' variable that is the instance
of the Dist::Zilla manpage currently running. Only those files listed in
'dist.ini' as 'filename = blah' will be considered templates. Filenames are
given relative to the root of the build.

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
%doc Changes META.yml LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*

