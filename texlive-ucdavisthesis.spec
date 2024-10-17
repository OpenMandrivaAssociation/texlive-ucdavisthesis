Name:		texlive-ucdavisthesis
Version:	40772
Release:	2
Summary:	A thesis/dissertation class for University of California Davis
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ucdavisthesis
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ucdavisthesis.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ucdavisthesis.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ucdavisthesis.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The class conforms to the University's requirements for 2009.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/ucdavisthesis
%doc %{_texmfdistdir}/doc/latex/ucdavisthesis
#- source
%doc %{_texmfdistdir}/source/latex/ucdavisthesis

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
