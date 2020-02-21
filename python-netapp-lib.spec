# what it's called on pypi
%global srcname netapp-lib
# what it's imported as
%global libname netapp_lib
# name of egg info directory
%global eggname %{libname}
# package name fragment
%global pkgname %{srcname}

%global common_description %{expand:
NetApp library for Python.}

Name:           python-%{srcname}
Version:        2019.12.20
Release:        1%{?dist}
Summary:        NetApp library for Python.
License:        Proprietary::NetApp
URL:            https://pypi.org/project/netapp-lib/
Source0:        %{pypi_source}

BuildArch:      noarch


%description %{common_description}
%package -n python%{python3_pkgversion}-%{pkgname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-lxml
BuildRequires:  python%{python3_pkgversion}-xmltodict
BuildRequires:  python%{python3_pkgversion}-requests
Requires: python%{python3_pkgversion}-lxml
Requires: python%{python3_pkgversion}-xmltodict
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pkgname}}


%description -n python%{python3_pkgversion}-%{pkgname} %{common_description}


%prep
%autosetup -n %{srcname}-%{version}
rm -rf %{eggname}.egg-info


%build
%py3_build

%install
%py3_install


# Note that there is no %%files section for the unversioned python module
%files -n python%{python3_pkgversion}-%{srcname}
%doc README.rst
%{python3_sitelib}/%{libname}
%{python3_sitelib}/%{eggname}-%{version}-py%{python3_version}.egg-info


%changelog
