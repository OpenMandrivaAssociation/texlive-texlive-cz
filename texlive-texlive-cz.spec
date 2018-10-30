Name:		texlive-texlive-cz
Version:	20180412
Release:	2
Summary:	TeX Live manual (Czech/Slovak)
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texlive-cz.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texlive-cz.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
TeXLive texlive-cz package.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/texlive/texlive-cz

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
