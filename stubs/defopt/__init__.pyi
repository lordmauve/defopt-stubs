from typing import Any, Callable, Literal

type Funcs[T] = Callable[..., T] | list[Callable[..., T]] | dict[str, Funcs[T]]

__version__: str

def run[T](
    funcs: Funcs[T],
    *,
    parsers: dict[type, Callable[[str], Any]] = ...,
    short: dict[str, str] | None = ...,
    cli_options: Literal["kwonly", "all", "has_default"] = ...,
    show_defaults: bool = ...,
    show_types: bool = ...,
    no_negated_flags: bool = ...,
    version: str | None | bool = ...,
    argparse_kwargs: dict = ...,
    intermixed: bool = ...,
    argv: list[str] | None = ...,
) -> T: ...

def bind[T](
    funcs: Funcs[T],
    *,
    parsers: dict[type, Callable[[str], Any]] = ...,
    short: dict[str, str] | None = ...,
    cli_options: Literal["kwonly", "all", "has_default"] = ...,
    show_defaults: bool = ...,
    show_types: bool = ...,
    no_negated_flags: bool = ...,
    version: str | None | bool = ...,
    argparse_kwargs: dict = ...,
    intermixed: bool = ...,
    argv: list[str] | None = ...,
) -> Callable[[], T]: ...

def bind_known[T](
    funcs: Funcs[T],
    *,
    parsers: dict[type, Callable[[str], Any]] = ...,
    short: dict[str, str] | None = ...,
    cli_options: Literal["kwonly", "all", "has_default"] = ...,
    show_defaults: bool = ...,
    show_types: bool = ...,
    no_negated_flags: bool = ...,
    version: str | None | bool = ...,
    argparse_kwargs: dict = ...,
    intermixed: bool = ...,
    argv: list[str] | None = ...,
) -> tuple[Callable[[], T], list[str]]: ...
