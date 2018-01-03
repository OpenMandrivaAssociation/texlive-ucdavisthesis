Name:		texlive-ucdavisthesis
Version:	1.3
Release:	1
Summary:	A thesis/dissertation class for University of California Davis
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ucdavisthesis
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ucdavisthesis.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ucdavisthesis.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ucdavisthesis.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
