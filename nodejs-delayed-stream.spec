%{?scl:%scl_package nodejs-delayed-stream}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

Name:           %{?scl_prefix}nodejs-delayed-stream
Version:        0.0.5
Release:        5%{?dist}
Summary:        Buffers events from a stream until you are ready to handle them
BuildArch:      noarch

Group:          System Environment/Libraries
License:        MIT
URL:            https://github.com/felixge/node-delayed-stream
Source0:        http://registry.npmjs.org/delayed-stream/-/delayed-stream-%{version}.tgz
BuildRoot:      %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  %{?scl_prefix}nodejs-devel

%description
Buffers events from a stream until you are ready to handle them.

%prep
%setup -q -n package

%build
#nothing to do

%install
rm -rf %buildroot
mkdir -p %{buildroot}%{nodejs_sitelib}/delayed-stream
cp -pr package.json lib %{buildroot}%{nodejs_sitelib}/delayed-stream

%clean
rm -rf %buildroot

%files
%defattr(-,root,root,-)
%{nodejs_sitelib}/delayed-stream
%doc License Readme.md

%changelog
* Thu Oct 17 2013 Tomas Hrcka <thrcka@redhat.com> - 0.0.5-5
- replace provides and requires with macro

* Thu Apr 11 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.0.5-4
- Add support for software collections

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.5-2
- add missing build section
- fix License

* Mon Dec 31 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.5-1
- initial package generated by npm2rpm
