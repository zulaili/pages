#!/usr/bin/env python
"""Generate static API documentation for GitHub Pages."""
import json
import os
from pathlib import Path

import django


def main(output_dir: str = "docs") -> None:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    django.setup()

    from config.api import api  # pylint: disable=import-outside-toplevel
    from scalar_django_ninja import (
        get_scalar_api_reference,
        scalar_theme,
    )  # pylint: disable=import-outside-toplevel

    project_root = Path(__file__).resolve().parent
    target = project_root / output_dir
    target.mkdir(parents=True, exist_ok=True)

    schema = api.get_openapi_schema()
    (target / "openapi.json").write_text(
        json.dumps(schema, indent=2),
        encoding="utf-8",
    )

    html_response = get_scalar_api_reference(
        openapi_url="openapi.json",
        title=api.title or "API Reference",
        scalar_js_url="https://cdn.jsdelivr.net/npm/@scalar/api-reference",
        scalar_proxy_url="",
        scalar_favicon_url="",
        scalar_theme=scalar_theme,
    )
    (target / "index.html").write_text(
        html_response.content.decode("utf-8"),
        encoding="utf-8",
    )

    print(f"Static docs written to {target}")


if __name__ == "__main__":
    main()
