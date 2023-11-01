%if 0%{?fedora} || 0%{?rhel} >= 8
%bcond_without python3
%else  # 0#{?fedora} || 0#{?rhel} >= 8
%bcond_with python3
%endif # 0#{?fedora} || 0#{?rhel} >= 8

%if 0%{?rhel} > 7
# Disable python2 build by default
%bcond_with python2
%else
%bcond_without python2
%endif

%global pypi_name argh
%global global_sum Unobtrusive argparse wrapper with natural syntax
%global global_desc							\
Building a command-line interface?  Found yourself uttering “argh!”	\
while struggling with the API of argparse?  Don’t want to lose its	\
power but don’t need the complexity?					\
									\
%{name} provides a wrapper for argparse.  Argparse is a very powerful	\
tool;  %{name} just makes it easy to use.


Name:		python-%{pypi_name}
Version:	0.26.1
Release:	8%{?dist}
Summary:	%{global_sum}

License:	LGPLv3+
URL:		https://pypi.python.org/pypi/%{pypi_name}
Source0:	https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
Source1:	https://www.gnu.org/licenses/lgpl-3.0.txt
Source2:	https://www.gnu.org/licenses/gpl-3.0.txt

# not upstreamed, fixes an assert in testsuite.
Patch0001:	python-argh-0.26.1-fix-testsuite.patch

BuildArch:	noarch

%description
%{global_desc}

%if %{with python2}
%package -n python2-%{pypi_name}
Summary:	%{global_sum}

BuildRequires:	python2-devel
BuildRequires:	python2-mock
%if %{with python3}
BuildRequires:	python2-pytest
%else  # with python3
BuildRequires:	pytest
%endif # with python3
BuildRequires:	python2-setuptools
%if 0%{?rhel} && 0%{?rhel} <= 6
BuildRequires:	python-argparse
Requires:	python-argparse
%endif

%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
%{global_desc}
%endif # with python2


%if %{with python3}
%package -n python3-%{pypi_name}
Summary:	%{global_sum}

BuildRequires:	python3-devel
BuildRequires:	python3-mock
BuildRequires:	python3-pytest
BuildRequires:	python3-setuptools

%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%{global_desc}
%endif # with python3


%prep
%autosetup -n %{pypi_name}-%{version} -p 1

%{__install} -pm 0644 %{SOURCE1} COPYING
%{__install} -pm 0644 %{SOURCE2} .


%build
%if %{with python2}
%py2_build
%endif # with python2
%if %{with python3}
%py3_build
%endif # with python3


%install
%if %{with python3}
%py3_install
%endif # with python3
%if %{with python2}
%py2_install
%endif # with python2


%check
# tests need UTF-8 encoding
LANG="en_US.UTF-8"
LC_CTYPE="en_US.UTF-8"
export LANG LC_CTYPE
%if %{with python2}
%{__python2} setup.py test
%endif # with python2
%if %{with python3}
%{__python3} setup.py test
%endif # with python3

%if %{with python2}
%files -n python2-%{pypi_name}
%doc README.rst
%license COPYING gpl-3.0.txt
%{python2_sitelib}/*
%endif # with python2


%if %{with python3}
%files -n python3-%{pypi_name}
%doc README.rst
%license COPYING gpl-3.0.txt
%{python3_sitelib}/*
%endif # with python3


%changelog
* Fri Jun 08 2018 Charalampos Stratakis <cstratak@redhat.com> - 0.26.1-8
- Conditionalize the python2 subpackage

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.26.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.26.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 20 2017 Björn Esser <besser82@fedoraproject.org> - 0.26.1-5
- Adapt spec-file to recent guidelines

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.26.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 20 2016 Miro Hrončok <mhroncok@redhat.com> - 0.26.1-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Feb 08 2016 Björn Esser <fedora@besser82.io> - 0.26.1-1
- new upstream-release (#1301580)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Nov 06 2015 Robert Kuska <rkuska@redhat.com> - 0.23.2-5
- Rebuilt for Python3.5 rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 27 2014 Kalev Lember <kalevlember@gmail.com> - 0.23.2-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Mon Aug 12 2013 Björn Esser <bjoern.esser@gmail.com> - 0.23.2-1
- Initial rpm release (#996186)
