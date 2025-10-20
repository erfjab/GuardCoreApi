from .core import RequestCore
from .types import (
    AdminToken,
    AdminResponse,
    AdminCreate,
    AdminCurrentUpdate,
    AdminUsageLogsResponse,
    AdminUpdate,
    SubscriptionResponse,
    SubscriptionCreate,
    SubscriptionStatsResponse,
    SubscriptionUpdate,
    SubscriptionUsageLogsResponse,
    NodeResponse,
    NodeCreate,
    NodeUpdate,
    NodeStatsResponse,
    ServiceCreate,
    ServiceResponse,
    ServiceUpdate,
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
            "/api/admins/current/usages",
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
            f"/api/admins/{username}/usages",
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

    @staticmethod
    async def get_all_subscriptions(access: str) -> list[SubscriptionResponse]:
        return await RequestCore.get(
            "/api/subscriptions",
            headers=RequestCore.generate_headers(access),
            response_model=SubscriptionResponse,
            use_list=True,
        )

    @staticmethod
    async def create_subscription(
        data: list[SubscriptionCreate], access: str
    ) -> SubscriptionResponse:
        return await RequestCore.post(
            "/api/subscriptions",
            headers=RequestCore.generate_headers(access),
            json=[item.dict() for item in data],
            response_model=SubscriptionResponse,
            use_list=True,
        )

    @staticmethod
    async def get_subscription_stats(access: str) -> SubscriptionStatsResponse:
        return await RequestCore.get(
            "/api/subscriptions/stats",
            headers=RequestCore.generate_headers(access),
            response_model=SubscriptionStatsResponse,
        )

    @staticmethod
    async def get_subscription(username: str, access: str) -> SubscriptionResponse:
        return await RequestCore.get(
            f"/api/subscriptions/{username}",
            headers=RequestCore.generate_headers(access),
            response_model=SubscriptionResponse,
        )

    @staticmethod
    async def update_subscription(
        username: str, data: SubscriptionUpdate, access: str
    ) -> SubscriptionResponse:
        return await RequestCore.put(
            f"/api/subscriptions/{username}",
            headers=RequestCore.generate_headers(access),
            json=data.dict(),
            response_model=SubscriptionResponse,
        )

    @staticmethod
    async def delete_subscription(username: str, access: str) -> dict:
        return await RequestCore.delete(
            f"/api/subscriptions/{username}",
            headers=RequestCore.generate_headers(access),
        )

    @staticmethod
    async def get_subscription_usages(
        username: str, access: str
    ) -> SubscriptionUsageLogsResponse:
        return await RequestCore.get(
            f"/api/subscriptions/{username}/usages",
            headers=RequestCore.generate_headers(access),
            response_model=SubscriptionUsageLogsResponse,
        )

    @staticmethod
    async def enable_subscription(username: str, access: str) -> SubscriptionResponse:
        return await RequestCore.post(
            f"/api/subscriptions/{username}/enable",
            headers=RequestCore.generate_headers(access),
            response_model=SubscriptionResponse,
        )

    @staticmethod
    async def disable_subscription(username: str, access: str) -> SubscriptionResponse:
        return await RequestCore.post(
            f"/api/subscriptions/{username}/disable",
            headers=RequestCore.generate_headers(access),
            response_model=SubscriptionResponse,
        )

    @staticmethod
    async def revoke_subscription(username: str, access: str) -> SubscriptionResponse:
        return await RequestCore.post(
            f"/api/subscriptions/{username}/revoke",
            headers=RequestCore.generate_headers(access),
            response_model=SubscriptionResponse,
        )

    @staticmethod
    async def reset_subscription(username: str, access: str) -> SubscriptionResponse:
        return await RequestCore.post(
            f"/api/subscriptions/{username}/reset",
            headers=RequestCore.generate_headers(access),
            response_model=SubscriptionResponse,
        )

    @staticmethod
    async def get_nodes(access: str) -> list[NodeResponse]:
        return await RequestCore.get(
            "/api/nodes",
            headers=RequestCore.generate_headers(access),
            response_model=NodeResponse,
            use_list=True,
        )

    @staticmethod
    async def create_node(data: NodeCreate, access: str) -> NodeResponse:
        return await RequestCore.post(
            "/api/nodes",
            headers=RequestCore.generate_headers(access),
            json=data.dict(),
            response_model=NodeResponse,
        )

    @staticmethod
    async def get_node_stats(access: str) -> NodeStatsResponse:
        return await RequestCore.get(
            "/api/nodes/stats",
            headers=RequestCore.generate_headers(access),
            response_model=NodeStatsResponse,
        )

    @staticmethod
    async def get_node(node_id: int, access: str) -> NodeResponse:
        return await RequestCore.get(
            f"/api/nodes/{node_id}",
            headers=RequestCore.generate_headers(access),
            response_model=NodeResponse,
        )

    @staticmethod
    async def update_node(node_id: int, data: NodeUpdate, access: str) -> NodeResponse:
        return await RequestCore.put(
            f"/api/nodes/{node_id}",
            headers=RequestCore.generate_headers(access),
            json=data.dict(),
            response_model=NodeResponse,
        )

    @staticmethod
    async def delete_node(node_id: int, access: str) -> dict:
        return await RequestCore.delete(
            f"/api/nodes/{node_id}",
            headers=RequestCore.generate_headers(access),
        )

    @staticmethod
    async def enable_node(node_id: int, access: str) -> NodeResponse:
        return await RequestCore.post(
            f"/api/nodes/{node_id}/enable",
            headers=RequestCore.generate_headers(access),
            response_model=NodeResponse,
        )

    @staticmethod
    async def disable_node(node_id: int, access: str) -> NodeResponse:
        return await RequestCore.post(
            f"/api/nodes/{node_id}/disable",
            headers=RequestCore.generate_headers(access),
            response_model=NodeResponse,
        )

    @staticmethod
    async def get_services(access: str) -> list[ServiceResponse]:
        return await RequestCore.get(
            "/api/services",
            headers=RequestCore.generate_headers(access),
            response_model=ServiceResponse,
            use_list=True,
        )

    @staticmethod
    async def create_service(data: ServiceCreate, access: str) -> ServiceResponse:
        return await RequestCore.post(
            "/api/services",
            headers=RequestCore.generate_headers(access),
            json=data.dict(),
            response_model=ServiceResponse,
        )

    @staticmethod
    async def get_service(service_id: int, access: str) -> ServiceResponse:
        return await RequestCore.get(
            f"/api/services/{service_id}",
            headers=RequestCore.generate_headers(access),
            response_model=ServiceResponse,
        )

    @staticmethod
    async def update_service(
        service_id: int, data: ServiceUpdate, access: str
    ) -> ServiceResponse:
        return await RequestCore.put(
            f"/api/services/{service_id}",
            headers=RequestCore.generate_headers(access),
            json=data.dict(),
            response_model=ServiceResponse,
        )

    @staticmethod
    async def delete_service(service_id: int, access: str) -> dict:
        return await RequestCore.delete(
            f"/api/services/{service_id}",
            headers=RequestCore.generate_headers(access),
        )

    @staticmethod
    async def get_guard(secret: str) -> list[str]:
        return await RequestCore.get(
            f"/api/guards/{secret}",
        )
