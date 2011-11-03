# revision 23147
# category TLCore
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-texlive-cz
Version:	20111103
Release:	1
Summary:	TeX Live manual (Czech/Slovak)
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texlive-cz.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texlive-cz.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
TeXLive texlive-cz package.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdir}/doc/texlive/texlive-cz/Makefile
%doc %{_texmfdir}/doc/texlive/texlive-cz/ec-lmr10-19.png
%doc %{_texmfdir}/doc/texlive/texlive-cz/live4ht.cfg
%doc %{_texmfdir}/doc/texlive/texlive-cz/tex-live.css
%doc %{_texmfdir}/doc/texlive/texlive-cz/texlive-cz.css
%doc %{_texmfdir}/doc/texlive/texlive-cz/texlive-cz.html
%doc %{_texmfdir}/doc/texlive/texlive-cz/texlive-cz.pdf
%doc %{_texmfdir}/doc/texlive/texlive-cz/texlive-cz.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
