# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "network express-route port list",
)
class List(AAZCommand):
    """List ExpressRoute ports.

    :example: List ExpressRoute ports. (autogenerated)
        az network express-route port list --resource-group myresourcegroup
    """

    _aaz_info = {
        "version": "2022-01-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/providers/microsoft.network/expressrouteports", "2022-01-01"],
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.network/expressrouteports", "2022-01-01"],
        ]
    }

    AZ_SUPPORT_PAGINATION = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_paging(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.resource_group = AAZResourceGroupNameArg()
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        condition_0 = has_value(self.ctx.args.resource_group) and has_value(self.ctx.subscription_id)
        condition_1 = has_value(self.ctx.subscription_id) and has_value(self.ctx.args.resource_group) is not True
        if condition_0:
            self.ExpressRoutePortsListByResourceGroup(ctx=self.ctx)()
        if condition_1:
            self.ExpressRoutePortsList(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance.value, client_flatten=True)
        next_link = self.deserialize_output(self.ctx.vars.instance.next_link)
        return result, next_link

    class ExpressRoutePortsListByResourceGroup(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/ExpressRoutePorts",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-01-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.next_link = AAZStrType(
                serialized_name="nextLink",
            )
            _schema_on_200.value = AAZListType()

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.etag = AAZStrType(
                flags={"read_only": True},
            )
            _element.id = AAZStrType()
            _element.identity = AAZObjectType()
            _element.location = AAZStrType()
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _element.tags = AAZDictType()
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            identity = cls._schema_on_200.value.Element.identity
            identity.principal_id = AAZStrType(
                serialized_name="principalId",
                flags={"read_only": True},
            )
            identity.tenant_id = AAZStrType(
                serialized_name="tenantId",
                flags={"read_only": True},
            )
            identity.type = AAZStrType()
            identity.user_assigned_identities = AAZDictType(
                serialized_name="userAssignedIdentities",
            )

            user_assigned_identities = cls._schema_on_200.value.Element.identity.user_assigned_identities
            user_assigned_identities.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.identity.user_assigned_identities.Element
            _element.client_id = AAZStrType(
                serialized_name="clientId",
                flags={"read_only": True},
            )
            _element.principal_id = AAZStrType(
                serialized_name="principalId",
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.value.Element.properties
            properties.allocation_date = AAZStrType(
                serialized_name="allocationDate",
                flags={"read_only": True},
            )
            properties.bandwidth_in_gbps = AAZIntType(
                serialized_name="bandwidthInGbps",
            )
            properties.circuits = AAZListType(
                flags={"read_only": True},
            )
            properties.encapsulation = AAZStrType()
            properties.ether_type = AAZStrType(
                serialized_name="etherType",
                flags={"read_only": True},
            )
            properties.links = AAZListType()
            properties.mtu = AAZStrType(
                flags={"read_only": True},
            )
            properties.peering_location = AAZStrType(
                serialized_name="peeringLocation",
            )
            properties.provisioned_bandwidth_in_gbps = AAZFloatType(
                serialized_name="provisionedBandwidthInGbps",
                flags={"read_only": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.resource_guid = AAZStrType(
                serialized_name="resourceGuid",
                flags={"read_only": True},
            )

            circuits = cls._schema_on_200.value.Element.properties.circuits
            circuits.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.circuits.Element
            _element.id = AAZStrType()

            links = cls._schema_on_200.value.Element.properties.links
            links.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.links.Element
            _element.etag = AAZStrType(
                flags={"read_only": True},
            )
            _element.id = AAZStrType()
            _element.name = AAZStrType()
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )

            properties = cls._schema_on_200.value.Element.properties.links.Element.properties
            properties.admin_state = AAZStrType(
                serialized_name="adminState",
            )
            properties.connector_type = AAZStrType(
                serialized_name="connectorType",
                flags={"read_only": True},
            )
            properties.interface_name = AAZStrType(
                serialized_name="interfaceName",
                flags={"read_only": True},
            )
            properties.mac_sec_config = AAZObjectType(
                serialized_name="macSecConfig",
            )
            properties.patch_panel_id = AAZStrType(
                serialized_name="patchPanelId",
                flags={"read_only": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.rack_id = AAZStrType(
                serialized_name="rackId",
                flags={"read_only": True},
            )
            properties.router_name = AAZStrType(
                serialized_name="routerName",
                flags={"read_only": True},
            )

            mac_sec_config = cls._schema_on_200.value.Element.properties.links.Element.properties.mac_sec_config
            mac_sec_config.cak_secret_identifier = AAZStrType(
                serialized_name="cakSecretIdentifier",
            )
            mac_sec_config.cipher = AAZStrType()
            mac_sec_config.ckn_secret_identifier = AAZStrType(
                serialized_name="cknSecretIdentifier",
            )
            mac_sec_config.sci_state = AAZStrType(
                serialized_name="sciState",
            )

            tags = cls._schema_on_200.value.Element.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200

    class ExpressRoutePortsList(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/providers/Microsoft.Network/ExpressRoutePorts",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-01-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.next_link = AAZStrType(
                serialized_name="nextLink",
            )
            _schema_on_200.value = AAZListType()

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.etag = AAZStrType(
                flags={"read_only": True},
            )
            _element.id = AAZStrType()
            _element.identity = AAZObjectType()
            _element.location = AAZStrType()
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _element.tags = AAZDictType()
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            identity = cls._schema_on_200.value.Element.identity
            identity.principal_id = AAZStrType(
                serialized_name="principalId",
                flags={"read_only": True},
            )
            identity.tenant_id = AAZStrType(
                serialized_name="tenantId",
                flags={"read_only": True},
            )
            identity.type = AAZStrType()
            identity.user_assigned_identities = AAZDictType(
                serialized_name="userAssignedIdentities",
            )

            user_assigned_identities = cls._schema_on_200.value.Element.identity.user_assigned_identities
            user_assigned_identities.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.identity.user_assigned_identities.Element
            _element.client_id = AAZStrType(
                serialized_name="clientId",
                flags={"read_only": True},
            )
            _element.principal_id = AAZStrType(
                serialized_name="principalId",
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.value.Element.properties
            properties.allocation_date = AAZStrType(
                serialized_name="allocationDate",
                flags={"read_only": True},
            )
            properties.bandwidth_in_gbps = AAZIntType(
                serialized_name="bandwidthInGbps",
            )
            properties.circuits = AAZListType(
                flags={"read_only": True},
            )
            properties.encapsulation = AAZStrType()
            properties.ether_type = AAZStrType(
                serialized_name="etherType",
                flags={"read_only": True},
            )
            properties.links = AAZListType()
            properties.mtu = AAZStrType(
                flags={"read_only": True},
            )
            properties.peering_location = AAZStrType(
                serialized_name="peeringLocation",
            )
            properties.provisioned_bandwidth_in_gbps = AAZFloatType(
                serialized_name="provisionedBandwidthInGbps",
                flags={"read_only": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.resource_guid = AAZStrType(
                serialized_name="resourceGuid",
                flags={"read_only": True},
            )

            circuits = cls._schema_on_200.value.Element.properties.circuits
            circuits.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.circuits.Element
            _element.id = AAZStrType()

            links = cls._schema_on_200.value.Element.properties.links
            links.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.links.Element
            _element.etag = AAZStrType(
                flags={"read_only": True},
            )
            _element.id = AAZStrType()
            _element.name = AAZStrType()
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )

            properties = cls._schema_on_200.value.Element.properties.links.Element.properties
            properties.admin_state = AAZStrType(
                serialized_name="adminState",
            )
            properties.connector_type = AAZStrType(
                serialized_name="connectorType",
                flags={"read_only": True},
            )
            properties.interface_name = AAZStrType(
                serialized_name="interfaceName",
                flags={"read_only": True},
            )
            properties.mac_sec_config = AAZObjectType(
                serialized_name="macSecConfig",
            )
            properties.patch_panel_id = AAZStrType(
                serialized_name="patchPanelId",
                flags={"read_only": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.rack_id = AAZStrType(
                serialized_name="rackId",
                flags={"read_only": True},
            )
            properties.router_name = AAZStrType(
                serialized_name="routerName",
                flags={"read_only": True},
            )

            mac_sec_config = cls._schema_on_200.value.Element.properties.links.Element.properties.mac_sec_config
            mac_sec_config.cak_secret_identifier = AAZStrType(
                serialized_name="cakSecretIdentifier",
            )
            mac_sec_config.cipher = AAZStrType()
            mac_sec_config.ckn_secret_identifier = AAZStrType(
                serialized_name="cknSecretIdentifier",
            )
            mac_sec_config.sci_state = AAZStrType(
                serialized_name="sciState",
            )

            tags = cls._schema_on_200.value.Element.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200


class _ListHelper:
    """Helper class for List"""


__all__ = ["List"]