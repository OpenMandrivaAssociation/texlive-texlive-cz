# revision 26864
# category TLCore
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-texlive-cz
Version:	20120808
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
%doc %{_texmfdir}/doc/texlive/texlive-cz/Makefile
%doc %{_texmfdir}/doc/texlive/texlive-cz/csquote.sty
%doc %{_texmfdir}/doc/texlive/texlive-cz/ec-lmr10-19.png
%doc %{_texmfdir}/doc/texlive/texlive-cz/live4ht.cfg
%doc %{_texmfdir}/doc/texlive/texlive-cz/tex-live.css
%doc %{_texmfdir}/doc/texlive/texlive-cz/texlive-cz.css
%doc %{_texmfdir}/doc/texlive/texlive-cz/texlive-cz.html
%doc %{_texmfdir}/doc/texlive/texlive-cz/texlive-cz.pdf
%doc %{_texmfdir}/doc/texlive/texlive-cz/texlive-cz.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf %{buildroot}%{_datadir}


%changelog
* Wed Aug 08 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120808-1
+ Revision: 812899
- Update to latest release.

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20111104-2
+ Revision: 756629
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20111104-1
+ Revision: 719692
- texlive-texlive-cz
- texlive-texlive-cz
- texlive-texlive-cz
- texlive-texlive-cz

