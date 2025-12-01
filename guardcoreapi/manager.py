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
    SubscriptionStatusStatsResponse,
    MostUsageSubscription,
    UsageStatsResponse,
    AgentStatsResponse,
)


class GuardCoreApi:
    @staticmethod
    async def get_all_admin(
        api_key: str | None = None, access_token: str | None = None
    ) -> list[AdminResponse]:
        return await RequestCore.get(
            "/api/admins",
            headers=RequestCore.generate_headers(api_key, access_token),
            response_model=AdminResponse,
            use_list=True,
        )

    @staticmethod
    async def create_admin(
        data: AdminCreate, api_key: str | None = None, access_token: str | None = None
    ) -> AdminResponse:
        return await RequestCore.post(
            "/api/admins",
            headers=RequestCore.generate_headers(api_key, access_token),
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
    async def get_current_admin(
        api_key: str | None = None, access_token: str | None = None
    ) -> AdminResponse:
        return await RequestCore.get(
            "/api/admins/current",
            headers=RequestCore.generate_headers(api_key, access_token),
            response_model=AdminResponse,
        )

    @staticmethod
    async def update_current_admin(
        data: AdminCurrentUpdate,
        api_key: str | None = None,
        access_token: str | None = None,
    ) -> AdminResponse:
        return await RequestCore.put(
            "/api/admins/current",
            headers=RequestCore.generate_headers(api_key, access_token),
            json=data.dict(),
            response_model=AdminResponse,
        )

    @staticmethod
    async def get_current_admin_usages(
        api_key: str | None = None, access_token: str | None = None
    ) -> AdminUsageLogsResponse:
        return await RequestCore.get(
            "/api/admins/current/usages",
            headers=RequestCore.generate_headers(api_key, access_token),
            response_model=AdminUsageLogsResponse,
        )

    @staticmethod
    async def revoke_current_admin_api_key(
        api_key: str | None = None, access_token: str | None = None
    ) -> AdminResponse:
        return await RequestCore.post(
            "/api/admins/current/revoke",
            headers=RequestCore.generate_headers(api_key, access_token),
            response_model=AdminResponse,
        )

    @staticmethod
    async def get_admin(
        username: str, api_key: str | None = None, access_token: str | None = None
    ) -> AdminResponse:
        return await RequestCore.get(
            f"/api/admins/{username}",
            headers=RequestCore.generate_headers(api_key, access_token),
            response_model=AdminResponse,
        )

    @staticmethod
    async def update_admin(
        username: str,
        data: AdminUpdate,
        api_key: str | None = None,
        access_token: str | None = None,
    ) -> AdminResponse:
        return await RequestCore.put(
            f"/api/admins/{username}",
            headers=RequestCore.generate_headers(api_key, access_token),
            json=data.dict(),
            response_model=AdminResponse,
        )

    @staticmethod
    async def delete_admin(
        username: str, api_key: str | None = None, access_token: str | None = None
    ) -> dict:
        return await RequestCore.delete(
            f"/api/admins/{username}",
            headers=RequestCore.generate_headers(api_key, access_token),
        )

    @staticmethod
    async def get_admin_usages(
        username: str, api_key: str | None = None, access_token: str | None = None
    ) -> AdminUsageLogsResponse:
        return await RequestCore.get(
            f"/api/admins/{username}/usages",
            headers=RequestCore.generate_headers(api_key, access_token),
            response_model=AdminUsageLogsResponse,
        )

    @staticmethod
    async def enable_admin(
        username: str, api_key: str | None = None, access_token: str | None = None
    ) -> AdminResponse:
        return await RequestCore.post(
            f"/api/admins/{username}/enable",
            headers=RequestCore.generate_headers(api_key, access_token),
            response_model=AdminResponse,
        )

    @staticmethod
    async def disable_admin(
        username: str, api_key: str | None = None, access_token: str | None = None
    ) -> AdminResponse:
        return await RequestCore.post(
            f"/api/admins/{username}/disable",
            headers=RequestCore.generate_headers(api_key, access_token),
            response_model=AdminResponse,
        )

    @staticmethod
    async def revoke_admin_api_key(
        username: str, api_key: str | None = None, access_token: str | None = None
    ) -> AdminResponse:
        return await RequestCore.post(
            f"/api/admins/{username}/revoke",
            headers=RequestCore.generate_headers(api_key, access_token),
            response_model=AdminResponse,
        )

    @staticmethod
    async def get_admin_subscriptions(
        username: str, api_key: str | None = None, access_token: str | None = None
    ) -> list[SubscriptionResponse]:
        return await RequestCore.get(
            f"/api/admins/{username}/subscriptions",
            headers=RequestCore.generate_headers(api_key, access_token),
            response_model=SubscriptionResponse,
            use_list=True,
        )

    @staticmethod
    async def revoke_admin(
        username: str, api_key: str | None = None, access_token: str | None = None
    ) -> dict:
        return await RequestCore.post(
            f"/api/admins/{username}/revoke",
            headers=RequestCore.generate_headers(api_key, access_token),
        )

    @staticmethod
    async def delete_admin_subscriptions(
        username: str, api_key: str | None = None, access_token: str | None = None
    ) -> dict:
        return await RequestCore.delete(
            f"/api/admins/{username}/subscriptions",
            headers=RequestCore.generate_headers(api_key, access_token),
        )

    @staticmethod
    async def activate_admin_subscriptions(
        username: str, api_key: str | None = None, access_token: str | None = None
    ) -> dict:
        return await RequestCore.post(
            f"/api/admins/{username}/subscriptions/activate",
            headers=RequestCore.generate_headers(api_key, access_token),
        )

    @staticmethod
    async def deactivate_admin_subscriptions(
        username: str, api_key: str | None = None, access_token: str | None = None
    ) -> dict:
        return await RequestCore.post(
            f"/api/admins/{username}/subscriptions/deactivate",
            headers=RequestCore.generate_headers(api_key, access_token),
        )

    @staticmethod
    async def get_all_subscriptions(
        api_key: str | None = None,
        access_token: str | None = None,
        limited: bool | None = None,
        expired: bool | None = None,
        is_active: bool | None = None,
        enabled: bool | None = None,
        search: str | None = None,
        online: bool | None = None,
        order_by: str | None = None,
        page: int | None = 1,
        size: int | None = 10,
    ) -> list[SubscriptionResponse]:
        params = {}
        if limited is not None:
            params["limited"] = limited
        if expired is not None:
            params["expired"] = expired
        if is_active is not None:
            params["is_active"] = is_active
        if enabled is not None:
            params["enabled"] = enabled
        if search is not None:
            params["search"] = search
        if online is not None:
            params["online"] = online
        if order_by is not None:
            params["order_by"] = order_by
        if page is not None:
            params["page"] = page
        if size is not None:
            params["size"] = size

        return await RequestCore.get(
            "/api/subscriptions",
            headers=RequestCore.generate_headers(api_key, access_token),
            params=params,
            response_model=SubscriptionResponse,
            use_list=True,
        )

    @staticmethod
    async def create_subscription(
        data: list[SubscriptionCreate],
        api_key: str | None = None,
        access_token: str | None = None,
    ) -> SubscriptionResponse:
        return await RequestCore.post(
            "/api/subscriptions",
            headers=RequestCore.generate_headers(api_key, access_token),
            json=[item.dict() for item in data],
            response_model=SubscriptionResponse,
            use_list=True,
        )

    @staticmethod
    async def get_subscription_count(
        api_key: str | None = None,
        access_token: str | None = None,
        limited: bool | None = None,
        expired: bool | None = None,
        is_active: bool | None = None,
        enabled: bool | None = None,
        online: bool | None = None,
    ) -> int:
        params = {}
        if limited is not None:
            params["limited"] = limited
        if expired is not None:
            params["expired"] = expired
        if is_active is not None:
            params["is_active"] = is_active
        if enabled is not None:
            params["enabled"] = enabled
        if online is not None:
            params["online"] = online

        return await RequestCore.get(
            "/api/subscriptions/count",
            headers=RequestCore.generate_headers(api_key, access_token),
            params=params,
        )

    @staticmethod
    async def get_subscription_stats(
        api_key: str | None = None, access_token: str | None = None
    ) -> SubscriptionStatsResponse:
        return await RequestCore.get(
            "/api/subscriptions/stats",
            headers=RequestCore.generate_headers(api_key, access_token),
            response_model=SubscriptionStatsResponse,
        )

    @staticmethod
    async def get_subscription(
        username: str, api_key: str | None = None, access_token: str | None = None
    ) -> SubscriptionResponse:
        return await RequestCore.get(
            f"/api/subscriptions/{username}",
            headers=RequestCore.generate_headers(api_key, access_token),
            response_model=SubscriptionResponse,
        )

    @staticmethod
    async def update_subscription(
        username: str,
        data: SubscriptionUpdate,
        api_key: str | None = None,
        access_token: str | None = None,
    ) -> SubscriptionResponse:
        return await RequestCore.put(
            f"/api/subscriptions/{username}",
            headers=RequestCore.generate_headers(api_key, access_token),
            json=data.dict(),
            response_model=SubscriptionResponse,
        )

    @staticmethod
    async def delete_subscription(
        username: str, api_key: str | None = None, access_token: str | None = None
    ) -> dict:
        return await RequestCore.delete(
            f"/api/subscriptions/{username}",
            headers=RequestCore.generate_headers(api_key, access_token),
        )

    @staticmethod
    async def get_subscription_usages(
        username: str, api_key: str | None = None, access_token: str | None = None
    ) -> SubscriptionUsageLogsResponse:
        return await RequestCore.get(
            f"/api/subscriptions/{username}/usages",
            headers=RequestCore.generate_headers(api_key, access_token),
            response_model=SubscriptionUsageLogsResponse,
        )

    @staticmethod
    async def enable_subscription(
        username: str, api_key: str | None = None, access_token: str | None = None
    ) -> SubscriptionResponse:
        return await RequestCore.post(
            f"/api/subscriptions/{username}/enable",
            headers=RequestCore.generate_headers(api_key, access_token),
            response_model=SubscriptionResponse,
        )

    @staticmethod
    async def disable_subscription(
        username: str, api_key: str | None = None, access_token: str | None = None
    ) -> SubscriptionResponse:
        return await RequestCore.post(
            f"/api/subscriptions/{username}/disable",
            headers=RequestCore.generate_headers(api_key, access_token),
            response_model=SubscriptionResponse,
        )

    @staticmethod
    async def revoke_subscription(
        username: str, api_key: str | None = None, access_token: str | None = None
    ) -> SubscriptionResponse:
        return await RequestCore.post(
            f"/api/subscriptions/{username}/revoke",
            headers=RequestCore.generate_headers(api_key, access_token),
            response_model=SubscriptionResponse,
        )

    @staticmethod
    async def reset_subscription(
        username: str, api_key: str | None = None, access_token: str | None = None
    ) -> SubscriptionResponse:
        return await RequestCore.post(
            f"/api/subscriptions/{username}/reset",
            headers=RequestCore.generate_headers(api_key, access_token),
            response_model=SubscriptionResponse,
        )

    @staticmethod
    async def bulk_add_service(
        service_id: int, api_key: str | None = None, access_token: str | None = None
    ) -> dict:
        return await RequestCore.post(
            f"/api/subscriptions/services/{service_id}",
            headers=RequestCore.generate_headers(api_key, access_token),
        )

    @staticmethod
    async def bulk_remove_service(
        service_id: int, api_key: str | None = None, access_token: str | None = None
    ) -> dict:
        return await RequestCore.delete(
            f"/api/subscriptions/services/{service_id}",
            headers=RequestCore.generate_headers(api_key, access_token),
        )

    @staticmethod
    async def get_nodes(
        api_key: str | None = None, access_token: str | None = None
    ) -> list[NodeResponse]:
        return await RequestCore.get(
            "/api/nodes",
            headers=RequestCore.generate_headers(api_key, access_token),
            response_model=NodeResponse,
            use_list=True,
        )

    @staticmethod
    async def create_node(
        data: NodeCreate, api_key: str | None = None, access_token: str | None = None
    ) -> NodeResponse:
        return await RequestCore.post(
            "/api/nodes",
            headers=RequestCore.generate_headers(api_key, access_token),
            json=data.dict(),
            response_model=NodeResponse,
        )

    @staticmethod
    async def get_node_stats(
        api_key: str | None = None, access_token: str | None = None
    ) -> NodeStatsResponse:
        return await RequestCore.get(
            "/api/nodes/stats",
            headers=RequestCore.generate_headers(api_key, access_token),
            response_model=NodeStatsResponse,
        )

    @staticmethod
    async def get_node(
        node_id: int, api_key: str | None = None, access_token: str | None = None
    ) -> NodeResponse:
        return await RequestCore.get(
            f"/api/nodes/{node_id}",
            headers=RequestCore.generate_headers(api_key, access_token),
            response_model=NodeResponse,
        )

    @staticmethod
    async def update_node(
        node_id: int,
        data: NodeUpdate,
        api_key: str | None = None,
        access_token: str | None = None,
    ) -> NodeResponse:
        return await RequestCore.put(
            f"/api/nodes/{node_id}",
            headers=RequestCore.generate_headers(api_key, access_token),
            json=data.dict(),
            response_model=NodeResponse,
        )

    @staticmethod
    async def delete_node(
        node_id: int, api_key: str | None = None, access_token: str | None = None
    ) -> dict:
        return await RequestCore.delete(
            f"/api/nodes/{node_id}",
            headers=RequestCore.generate_headers(api_key, access_token),
        )

    @staticmethod
    async def enable_node(
        node_id: int, api_key: str | None = None, access_token: str | None = None
    ) -> NodeResponse:
        return await RequestCore.post(
            f"/api/nodes/{node_id}/enable",
            headers=RequestCore.generate_headers(api_key, access_token),
            response_model=NodeResponse,
        )

    @staticmethod
    async def disable_node(
        node_id: int, api_key: str | None = None, access_token: str | None = None
    ) -> NodeResponse:
        return await RequestCore.post(
            f"/api/nodes/{node_id}/disable",
            headers=RequestCore.generate_headers(api_key, access_token),
            response_model=NodeResponse,
        )

    @staticmethod
    async def get_services(
        api_key: str | None = None, access_token: str | None = None
    ) -> list[ServiceResponse]:
        return await RequestCore.get(
            "/api/services",
            headers=RequestCore.generate_headers(api_key, access_token),
            response_model=ServiceResponse,
            use_list=True,
        )

    @staticmethod
    async def create_service(
        data: ServiceCreate, api_key: str | None = None, access_token: str | None = None
    ) -> ServiceResponse:
        return await RequestCore.post(
            "/api/services",
            headers=RequestCore.generate_headers(api_key, access_token),
            json=data.dict(),
            response_model=ServiceResponse,
        )

    @staticmethod
    async def get_service(
        service_id: int, api_key: str | None = None, access_token: str | None = None
    ) -> ServiceResponse:
        return await RequestCore.get(
            f"/api/services/{service_id}",
            headers=RequestCore.generate_headers(api_key, access_token),
            response_model=ServiceResponse,
        )

    @staticmethod
    async def update_service(
        service_id: int,
        data: ServiceUpdate,
        api_key: str | None = None,
        access_token: str | None = None,
    ) -> ServiceResponse:
        return await RequestCore.put(
            f"/api/services/{service_id}",
            headers=RequestCore.generate_headers(api_key, access_token),
            json=data.dict(),
            response_model=ServiceResponse,
        )

    @staticmethod
    async def delete_service(
        service_id: int, api_key: str | None = None, access_token: str | None = None
    ) -> dict:
        return await RequestCore.delete(
            f"/api/services/{service_id}",
            headers=RequestCore.generate_headers(api_key, access_token),
        )

    @staticmethod
    async def get_guard(secret: str) -> list[str]:
        return await RequestCore.get(
            f"/guards/{secret}",
        )

    @staticmethod
    async def get_guard_info(secret: str) -> SubscriptionResponse:
        return await RequestCore.get(
            f"/guards/{secret}/info",
        )

    @staticmethod
    async def get_guard_usage_logs(secret: str) -> SubscriptionUsageLogsResponse:
        return await RequestCore.get(
            f"/guards/{secret}/usages",
            response_model=SubscriptionUsageLogsResponse,
        )

    @staticmethod
    async def get_subscription_status_stats(
        api_key: str | None = None, access_token: str | None = None
    ) -> SubscriptionStatusStatsResponse:
        return await RequestCore.get(
            "/api/stats/subscriptions/status",
            headers=RequestCore.generate_headers(api_key, access_token),
            response_model=SubscriptionStatusStatsResponse,
        )

    @staticmethod
    async def get_most_usage_subscriptions(
        start_date: str,
        end_date: str,
        api_key: str | None = None,
        access_token: str | None = None,
    ) -> MostUsageSubscription:
        return await RequestCore.get(
            "/api/stats/subscriptions/most_usage",
            headers=RequestCore.generate_headers(api_key, access_token),
            params={"start_date": start_date, "end_date": end_date},
            response_model=MostUsageSubscription,
        )

    @staticmethod
    async def get_usage_stats(
        start_date: str,
        end_date: str,
        api_key: str | None = None,
        access_token: str | None = None,
    ) -> UsageStatsResponse:
        return await RequestCore.get(
            "/api/stats/usage",
            headers=RequestCore.generate_headers(api_key, access_token),
            params={"start_date": start_date, "end_date": end_date},
            response_model=UsageStatsResponse,
        )

    @staticmethod
    async def get_agent_stats(
        api_key: str | None = None, access_token: str | None = None
    ) -> AgentStatsResponse:
        return await RequestCore.get(
            "/api/stats/agents",
            headers=RequestCore.generate_headers(api_key, access_token),
            response_model=AgentStatsResponse,
        )
