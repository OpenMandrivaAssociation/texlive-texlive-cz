# revision 33936
# category TLCore
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-texlive-cz
Version:	20140621
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
%doc %{_texmfdistdir}/doc/texlive/texlive-cz/Makefile
%doc %{_texmfdistdir}/doc/texlive/texlive-cz/csquote.sty
%doc %{_texmfdistdir}/doc/texlive/texlive-cz/ec-lmr10-19.png
%doc %{_texmfdistdir}/doc/texlive/texlive-cz/live4ht.cfg
%doc %{_texmfdistdir}/doc/texlive/texlive-cz/tex-live.css
%doc %{_texmfdistdir}/doc/texlive/texlive-cz/texlive-cz.css
%doc %{_texmfdistdir}/doc/texlive/texlive-cz/texlive-cz.html
%doc %{_texmfdistdir}/doc/texlive/texlive-cz/texlive-cz.pdf
%doc %{_texmfdistdir}/doc/texlive/texlive-cz/texlive-cz.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
