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
    StatsResponse,
)


class GuardCoreApi:
    @staticmethod
    async def get_all_admin(api_key: str) -> list[AdminResponse]:
        return await RequestCore.get(
            "/api/admins",
            headers=RequestCore.generate_headers(api_key),
            response_model=AdminResponse,
            use_list=True,
        )

    @staticmethod
    async def create_admin(data: AdminCreate, api_key: str) -> AdminResponse:
        return await RequestCore.post(
            "/api/admins",
            headers=RequestCore.generate_headers(api_key),
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
    async def get_current_admin(api_key: str) -> AdminResponse:
        return await RequestCore.get(
            "/api/admins/current",
            headers=RequestCore.generate_headers(api_key),
            response_model=AdminResponse,
        )

    @staticmethod
    async def update_current_admin(
        data: AdminCurrentUpdate, api_key: str
    ) -> AdminResponse:
        return await RequestCore.put(
            "/api/admins/current",
            headers=RequestCore.generate_headers(api_key),
            json=data.dict(),
            response_model=AdminResponse,
        )

    @staticmethod
    async def get_current_admin_usages(api_key: str) -> dict:
        return await RequestCore.get(
            "/api/admins/current/usages",
            headers=RequestCore.generate_headers(api_key),
            response_model=AdminUsageLogsResponse,
        )

    @staticmethod
    async def get_admin(username: str, api_key: str) -> AdminResponse:
        return await RequestCore.get(
            f"/api/admins/{username}",
            headers=RequestCore.generate_headers(api_key),
            response_model=AdminResponse,
        )

    @staticmethod
    async def update_admin(
        username: str, data: AdminUpdate, api_key: str
    ) -> AdminResponse:
        return await RequestCore.put(
            f"/api/admins/{username}",
            headers=RequestCore.generate_headers(api_key),
            json=data.dict(),
            response_model=AdminResponse,
        )

    @staticmethod
    async def delete_admin(username: str, api_key: str) -> dict:
        return await RequestCore.post(
            f"/api/admins/{username}/delete",
            headers=RequestCore.generate_headers(api_key),
        )

    @staticmethod
    async def get_admin_usages(username: str, api_key: str) -> dict:
        return await RequestCore.get(
            f"/api/admins/{username}/usages",
            headers=RequestCore.generate_headers(api_key),
            response_model=AdminUsageLogsResponse,
        )

    @staticmethod
    async def enable_admin(username: str, api_key: str) -> AdminResponse:
        return await RequestCore.post(
            f"/api/admins/{username}/enable",
            headers=RequestCore.generate_headers(api_key),
            response_model=AdminResponse,
        )

    @staticmethod
    async def disable_admin(username: str, api_key: str) -> AdminResponse:
        return await RequestCore.post(
            f"/api/admins/{username}/disable",
            headers=RequestCore.generate_headers(api_key),
            response_model=AdminResponse,
        )

    @staticmethod
    async def get_admin_subscriptions(
        username: str, api_key: str
    ) -> list[SubscriptionResponse]:
        return await RequestCore.get(
            f"/api/admins/{username}/subscriptions",
            headers=RequestCore.generate_headers(api_key),
            response_model=SubscriptionResponse,
            use_list=True,
        )

    @staticmethod
    async def revoke_admin(username: str, api_key: str) -> dict:
        return await RequestCore.post(
            f"/api/admins/{username}/revoke",
            headers=RequestCore.generate_headers(api_key),
        )

    @staticmethod
    async def delete_admin_subscriptions(username: str, api_key: str) -> dict:
        return await RequestCore.delete(
            f"/api/admins/{username}/subscriptions",
            headers=RequestCore.generate_headers(api_key),
        )

    @staticmethod
    async def activate_admin_subscriptions(username: str, api_key: str) -> dict:
        return await RequestCore.post(
            f"/api/admins/{username}/subscriptions/activate",
            headers=RequestCore.generate_headers(api_key),
        )

    @staticmethod
    async def deactivate_admin_subscriptions(username: str, api_key: str) -> dict:
        return await RequestCore.post(
            f"/api/admins/{username}/subscriptions/deactivate",
            headers=RequestCore.generate_headers(api_key),
        )

    @staticmethod
    async def get_all_subscriptions(api_key: str) -> list[SubscriptionResponse]:
        return await RequestCore.get(
            "/api/subscriptions",
            headers=RequestCore.generate_headers(api_key),
            response_model=SubscriptionResponse,
            use_list=True,
        )

    @staticmethod
    async def create_subscription(
        data: list[SubscriptionCreate], api_key: str
    ) -> SubscriptionResponse:
        return await RequestCore.post(
            "/api/subscriptions",
            headers=RequestCore.generate_headers(api_key),
            json=[item.dict() for item in data],
            response_model=SubscriptionResponse,
            use_list=True,
        )

    @staticmethod
    async def get_subscription_stats(api_key: str) -> SubscriptionStatsResponse:
        return await RequestCore.get(
            "/api/subscriptions/stats",
            headers=RequestCore.generate_headers(api_key),
            response_model=SubscriptionStatsResponse,
        )

    @staticmethod
    async def get_subscription(username: str, api_key: str) -> SubscriptionResponse:
        return await RequestCore.get(
            f"/api/subscriptions/{username}",
            headers=RequestCore.generate_headers(api_key),
            response_model=SubscriptionResponse,
        )

    @staticmethod
    async def update_subscription(
        username: str, data: SubscriptionUpdate, api_key: str
    ) -> SubscriptionResponse:
        return await RequestCore.put(
            f"/api/subscriptions/{username}",
            headers=RequestCore.generate_headers(api_key),
            json=data.dict(),
            response_model=SubscriptionResponse,
        )

    @staticmethod
    async def delete_subscription(username: str, api_key: str) -> dict:
        return await RequestCore.delete(
            f"/api/subscriptions/{username}",
            headers=RequestCore.generate_headers(api_key),
        )

    @staticmethod
    async def get_subscription_usages(
        username: str, api_key: str
    ) -> SubscriptionUsageLogsResponse:
        return await RequestCore.get(
            f"/api/subscriptions/{username}/usages",
            headers=RequestCore.generate_headers(api_key),
            response_model=SubscriptionUsageLogsResponse,
        )

    @staticmethod
    async def enable_subscription(username: str, api_key: str) -> SubscriptionResponse:
        return await RequestCore.post(
            f"/api/subscriptions/{username}/enable",
            headers=RequestCore.generate_headers(api_key),
            response_model=SubscriptionResponse,
        )

    @staticmethod
    async def disable_subscription(username: str, api_key: str) -> SubscriptionResponse:
        return await RequestCore.post(
            f"/api/subscriptions/{username}/disable",
            headers=RequestCore.generate_headers(api_key),
            response_model=SubscriptionResponse,
        )

    @staticmethod
    async def revoke_subscription(username: str, api_key: str) -> SubscriptionResponse:
        return await RequestCore.post(
            f"/api/subscriptions/{username}/revoke",
            headers=RequestCore.generate_headers(api_key),
            response_model=SubscriptionResponse,
        )

    @staticmethod
    async def reset_subscription(username: str, api_key: str) -> SubscriptionResponse:
        return await RequestCore.post(
            f"/api/subscriptions/{username}/reset",
            headers=RequestCore.generate_headers(api_key),
            response_model=SubscriptionResponse,
        )

    @staticmethod
    async def get_nodes(api_key: str) -> list[NodeResponse]:
        return await RequestCore.get(
            "/api/nodes",
            headers=RequestCore.generate_headers(api_key),
            response_model=NodeResponse,
            use_list=True,
        )

    @staticmethod
    async def create_node(data: NodeCreate, api_key: str) -> NodeResponse:
        return await RequestCore.post(
            "/api/nodes",
            headers=RequestCore.generate_headers(api_key),
            json=data.dict(),
            response_model=NodeResponse,
        )

    @staticmethod
    async def get_node_stats(api_key: str) -> NodeStatsResponse:
        return await RequestCore.get(
            "/api/nodes/stats",
            headers=RequestCore.generate_headers(api_key),
            response_model=NodeStatsResponse,
        )

    @staticmethod
    async def get_node(node_id: int, api_key: str) -> NodeResponse:
        return await RequestCore.get(
            f"/api/nodes/{node_id}",
            headers=RequestCore.generate_headers(api_key),
            response_model=NodeResponse,
        )

    @staticmethod
    async def update_node(node_id: int, data: NodeUpdate, api_key: str) -> NodeResponse:
        return await RequestCore.put(
            f"/api/nodes/{node_id}",
            headers=RequestCore.generate_headers(api_key),
            json=data.dict(),
            response_model=NodeResponse,
        )

    @staticmethod
    async def delete_node(node_id: int, api_key: str) -> dict:
        return await RequestCore.delete(
            f"/api/nodes/{node_id}",
            headers=RequestCore.generate_headers(api_key),
        )

    @staticmethod
    async def enable_node(node_id: int, api_key: str) -> NodeResponse:
        return await RequestCore.post(
            f"/api/nodes/{node_id}/enable",
            headers=RequestCore.generate_headers(api_key),
            response_model=NodeResponse,
        )

    @staticmethod
    async def disable_node(node_id: int, api_key: str) -> NodeResponse:
        return await RequestCore.post(
            f"/api/nodes/{node_id}/disable",
            headers=RequestCore.generate_headers(api_key),
            response_model=NodeResponse,
        )

    @staticmethod
    async def get_services(api_key: str) -> list[ServiceResponse]:
        return await RequestCore.get(
            "/api/services",
            headers=RequestCore.generate_headers(api_key),
            response_model=ServiceResponse,
            use_list=True,
        )

    @staticmethod
    async def create_service(data: ServiceCreate, api_key: str) -> ServiceResponse:
        return await RequestCore.post(
            "/api/services",
            headers=RequestCore.generate_headers(api_key),
            json=data.dict(),
            response_model=ServiceResponse,
        )

    @staticmethod
    async def get_service(service_id: int, api_key: str) -> ServiceResponse:
        return await RequestCore.get(
            f"/api/services/{service_id}",
            headers=RequestCore.generate_headers(api_key),
            response_model=ServiceResponse,
        )

    @staticmethod
    async def update_service(
        service_id: int, data: ServiceUpdate, api_key: str
    ) -> ServiceResponse:
        return await RequestCore.put(
            f"/api/services/{service_id}",
            headers=RequestCore.generate_headers(api_key),
            json=data.dict(),
            response_model=ServiceResponse,
        )

    @staticmethod
    async def delete_service(service_id: int, api_key: str) -> dict:
        return await RequestCore.delete(
            f"/api/services/{service_id}",
            headers=RequestCore.generate_headers(api_key),
        )

    @staticmethod
    async def get_guard(secret: str) -> list[str]:
        return await RequestCore.get(
            f"/api/guards/{secret}",
        )

    @staticmethod
    async def get_guard_info(secret: str) -> SubscriptionResponse:
        return await RequestCore.get(
            f"/api/guards/{secret}/info",
        )

    @staticmethod
    async def get_guard_usage_logs(secret: str) -> SubscriptionUsageLogsResponse:
        return await RequestCore.get(
            f"/api/guards/{secret}/usages",
            response_model=SubscriptionUsageLogsResponse,
        )

    @staticmethod
    async def get_stats(api_key: str) -> StatsResponse:
        return await RequestCore.get(
            "/api/stats",
            headers=RequestCore.generate_headers(api_key),
            response_model=StatsResponse,
        )
