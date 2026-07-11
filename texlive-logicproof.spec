%global tl_name logicproof
%global tl_revision 33254

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Box proofs for propositional and predicate logic
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/logicproof
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/logicproof.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/logicproof.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/logicproof.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A common style of proof used in propositional and predicate logic is
Fitch proofs, in which each line of the proof has a statement and a
justification, and subproofs within a larger proof have boxes around
them. The package provides environments for typesetting such proofs and
boxes. It creates proofs in a style similar to that used in "Logic in
Computer Science" by Huth and Ryan.

