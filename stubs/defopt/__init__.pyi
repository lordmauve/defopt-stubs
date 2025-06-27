from typing import Any, Callable, Dict, List, Optional, Union, Literal, Tuple

Funcs = Union[Callable[..., Any], List[Callable[..., Any]], Dict[str, "Funcs"]]

__version__: str

def run(
    funcs: Funcs,
    *,
    parsers: Dict[type, Callable[[str], Any]] = ..., 
    short: Optional[Dict[str, str]] = ..., 
    cli_options: Literal["kwonly", "all", "has_default"] = ..., 
    show_defaults: bool = ..., 
    show_types: bool = ..., 
    no_negated_flags: bool = ..., 
    version: Union[str, None, bool] = ..., 
    argparse_kwargs: dict = ..., 
    intermixed: bool = ..., 
    argv: Optional[List[str]] = ...,
) -> Any: ...

def bind(
    funcs: Funcs,
    *,
    parsers: Dict[type, Callable[[str], Any]] = ...,
    short: Optional[Dict[str, str]] = ..., 
    cli_options: Literal["kwonly", "all", "has_default"] = ..., 
    show_defaults: bool = ..., 
    show_types: bool = ..., 
    no_negated_flags: bool = ..., 
    version: Union[str, None, bool] = ..., 
    argparse_kwargs: dict = ..., 
    intermixed: bool = ..., 
    argv: Optional[List[str]] = ...,
) -> Callable[[], Any]: ...

def bind_known(
    funcs: Funcs,
    *,
    parsers: Dict[type, Callable[[str], Any]] = ...,
    short: Optional[Dict[str, str]] = ..., 
    cli_options: Literal["kwonly", "all", "has_default"] = ..., 
    show_defaults: bool = ..., 
    show_types: bool = ..., 
    no_negated_flags: bool = ..., 
    version: Union[str, None, bool] = ..., 
    argparse_kwargs: dict = ..., 
    intermixed: bool = ..., 
    argv: Optional[List[str]] = ...,
) -> Tuple[Callable[[], Any], List[str]]: ...
