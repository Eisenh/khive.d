from typing import Literal

from pydantic import SecretStr

AUTH_TYPES = Literal["bearer", "x-api-key"]


class HeaderFactory:
    @staticmethod
    def get_content_type_header(
        content_type: str = "application/json",
    ) -> dict[str, str]:
        return {"Content-Type": content_type}

    @staticmethod
    def get_bearer_auth_header(api_key: str) -> dict[str, str]:
        return {"Authorization": f"Bearer {api_key}"}

    @staticmethod
    def get_x_api_key_header(api_key: str) -> dict[str, str]:
        return {"x-api-key": api_key}

    @staticmethod
    def get_header(
        auth_type: AUTH_TYPES,
        content_type: str = "application/json",
        api_key: str | SecretStr | None = None,
        default_headers: dict[str, str] | None = None,
    ) -> dict[str, str]:
        if not api_key:
            raise ValueError("API key is required for authentication")

        api_key = (
            api_key.get_secret_value() if isinstance(api_key, SecretStr) else api_key
        )
        dict_ = HeaderFactory.get_content_type_header(content_type)
        if auth_type == "bearer":
            dict_.update(HeaderFactory.get_bearer_auth_header(api_key))
        elif auth_type == "x-api-key":
            dict_.update(HeaderFactory.get_x_api_key_header(api_key))
        else:
            raise ValueError(f"Unsupported auth type: {auth_type}")

        if default_headers:
            dict_.update(default_headers)
        return dict_
