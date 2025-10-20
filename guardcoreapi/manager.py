from .core import RequestCore
from .types import (
    AdminToken,
    AdminResponse,
    AdminCreate,
    AdminCurrentUpdate,
    AdminUsageLogsResponse,
    AdminUpdate,
    SubscriptionResponse,
)


class GuardCoreApi:
    @staticmethod
    async def get_all_admin(access: str) -> list[AdminResponse]:
        return await RequestCore.get(
            "/api/admins",
            headers=RequestCore.generate_headers(access),
            response_model=AdminResponse,
            use_list=True,
        )

    @staticmethod
    async def create_admin(data: AdminCreate, access: str) -> AdminResponse:
        return await RequestCore.post(
            "/api/admins",
            headers=RequestCore.generate_headers(access),
            json=data.dict(),
            response_model=AdminResponse,
        )

    @staticmethod
    async def generate_admin_token(username: str, password: str) -> AdminToken:
        return await RequestCore.post(
            "/api/admins/token",
            data={
                "username": username,
                "password": password,
            },
            response_model=AdminToken,
        )

    @staticmethod
    async def get_current_admin(access: str) -> AdminResponse:
        return await RequestCore.get(
            "/api/admins/current",
            headers=RequestCore.generate_headers(access),
            response_model=AdminResponse,
        )

    @staticmethod
    async def update_current_admin(
        data: AdminCurrentUpdate, access: str
    ) -> AdminResponse:
        return await RequestCore.put(
            "/api/admins/current",
            headers=RequestCore.generate_headers(access),
            json=data.dict(),
            response_model=AdminResponse,
        )

    @staticmethod
    async def get_current_admin_usages(access: str) -> dict:
        return await RequestCore.get(
            "/api/admins/current/usage",
            headers=RequestCore.generate_headers(access),
            response_model=AdminUsageLogsResponse,
        )

    @staticmethod
    async def get_admin(username: str, access: str) -> AdminResponse:
        return await RequestCore.get(
            f"/api/admins/{username}",
            headers=RequestCore.generate_headers(access),
            response_model=AdminResponse,
        )

    @staticmethod
    async def update_admin(
        username: str, data: AdminUpdate, access: str
    ) -> AdminResponse:
        return await RequestCore.put(
            f"/api/admins/{username}",
            headers=RequestCore.generate_headers(access),
            json=data.dict(),
            response_model=AdminResponse,
        )

    @staticmethod
    async def delete_admin(username: str, access: str) -> dict:
        return await RequestCore.post(
            f"/api/admins/{username}/delete",
            headers=RequestCore.generate_headers(access),
        )

    @staticmethod
    async def get_admin_usages(username: str, access: str) -> dict:
        return await RequestCore.get(
            f"/api/admins/{username}/usage",
            headers=RequestCore.generate_headers(access),
            response_model=AdminUsageLogsResponse,
        )

    @staticmethod
    async def enable_admin(username: str, access: str) -> AdminResponse:
        return await RequestCore.post(
            f"/api/admins/{username}/enable",
            headers=RequestCore.generate_headers(access),
            response_model=AdminResponse,
        )

    @staticmethod
    async def disable_admin(username: str, access: str) -> AdminResponse:
        return await RequestCore.post(
            f"/api/admins/{username}/disable",
            headers=RequestCore.generate_headers(access),
            response_model=AdminResponse,
        )

    @staticmethod
    async def get_admin_subscriptions(
        username: str, access: str
    ) -> list[SubscriptionResponse]:
        return await RequestCore.get(
            f"/api/admins/{username}/subscriptions",
            headers=RequestCore.generate_headers(access),
            response_model=SubscriptionResponse,
            use_list=True,
        )

    @staticmethod
    async def delete_admin_subscriptions(username: str, access: str) -> dict:
        return await RequestCore.delete(
            f"/api/admins/{username}/subscriptions",
            headers=RequestCore.generate_headers(access),
        )

    @staticmethod
    async def activate_admin_subscriptions(username: str, access: str) -> dict:
        return await RequestCore.post(
            f"/api/admins/{username}/subscriptions/activate",
            headers=RequestCore.generate_headers(access),
        )

    @staticmethod
    async def deactivate_admin_subscriptions(username: str, access: str) -> dict:
        return await RequestCore.post(
            f"/api/admins/{username}/subscriptions/deactivate",
            headers=RequestCore.generate_headers(access),
        )
