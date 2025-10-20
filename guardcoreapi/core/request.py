import asyncio
from typing import Optional

import aiohttp
from .exceptions import (
    RequestAuthenticationError,
    RequestConnectionError,
    RequestResponseError,
    RequestTimeoutError,
)


class RequestCore:
    _BASE_URL = "https://core.erfjab.com/"

    @staticmethod
    def generate_headers(access_token: Optional[str] = None) -> dict:
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
        if access_token:
            headers["Authorization"] = f"Bearer {access_token}"
        return headers

    @staticmethod
    async def fetch(
        endpoint: str,
        method: str = "GET",
        headers: Optional[dict] = None,
        params: Optional[dict] = None,
        data: Optional[dict] = None,
        json: Optional[dict] = None,
        timeout: float = 10.0,
    ) -> dict:
        try:
            async with aiohttp.ClientSession(
                timeout=aiohttp.ClientTimeout(total=timeout)
            ) as session:
                async with session.request(
                    method=method,
                    url=RequestCore._BASE_URL + endpoint,
                    headers=headers,
                    params=params,
                    data=data,
                    json=json,
                ) as response:
                    response.raise_for_status()
                    return await response.json()
        except aiohttp.ClientResponseError as e:
            if e.status == 401:
                raise RequestAuthenticationError("Authentication failed") from e
            else:
                raise RequestResponseError(f"Invalid response: {e.status}") from e
        except aiohttp.ClientConnectionError as e:
            raise RequestConnectionError("Connection error occurred") from e
        except asyncio.TimeoutError as e:
            raise RequestTimeoutError("Request timed out") from e

    @staticmethod
    async def get(
        endpoint: str,
        headers: Optional[dict] = None,
        params: Optional[dict] = None,
        timeout: float = 10.0,
    ) -> dict:
        return await RequestCore.fetch(
            endpoint=endpoint,
            method="GET",
            headers=headers,
            params=params,
            timeout=timeout,
        )

    @staticmethod
    async def post(
        endpoint: str,
        headers: Optional[dict] = None,
        data: Optional[dict] = None,
        json: Optional[dict] = None,
        timeout: float = 10.0,
    ) -> dict:
        return await RequestCore.fetch(
            endpoint=endpoint,
            method="POST",
            headers=headers,
            data=data,
            json=json,
            timeout=timeout,
        )

    @staticmethod
    async def put(
        endpoint: str,
        headers: Optional[dict] = None,
        data: Optional[dict] = None,
        json: Optional[dict] = None,
        timeout: float = 10.0,
    ) -> dict:
        return await RequestCore.fetch(
            endpoint=endpoint,
            method="PUT",
            headers=headers,
            data=data,
            json=json,
            timeout=timeout,
        )

    @staticmethod
    async def delete(
        endpoint: str,
        headers: Optional[dict] = None,
        timeout: float = 10.0,
    ) -> dict:
        return await RequestCore.fetch(
            endpoint=endpoint,
            method="DELETE",
            headers=headers,
            timeout=timeout,
        )
