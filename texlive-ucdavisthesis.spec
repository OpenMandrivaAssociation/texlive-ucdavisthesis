%global tl_name ucdavisthesis
%global tl_revision 40772

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.3
Release:	%{tl_revision}.1
Summary:	A thesis/dissertation class for University of California at Davis
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ucdavisthesis
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ucdavisthesis.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ucdavisthesis.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ucdavisthesis.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The ucdavisthesis class is a LaTeX class that allows you to create a
dissertation or thesis conforming to UC Davis formatting requirements as
of April 2016.

