# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from sandbox import Sandbox, AsyncSandbox

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRoot:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Sandbox) -> None:
        root = client.root.retrieve()
        assert root is None

    @parametrize
    def test_raw_response_retrieve(self, client: Sandbox) -> None:
        response = client.root.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        root = response.parse()
        assert root is None

    @parametrize
    def test_streaming_response_retrieve(self, client: Sandbox) -> None:
        with client.root.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            root = response.parse()
            assert root is None

        assert cast(Any, response.is_closed) is True


class TestAsyncRoot:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSandbox) -> None:
        root = await async_client.root.retrieve()
        assert root is None

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSandbox) -> None:
        response = await async_client.root.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        root = await response.parse()
        assert root is None

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSandbox) -> None:
        async with async_client.root.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            root = await response.parse()
            assert root is None

        assert cast(Any, response.is_closed) is True
