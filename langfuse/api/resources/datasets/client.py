# This file was auto-generated by Fern from our API Definition.

import typing
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...core.pydantic_utilities import pydantic_v1
from ...core.request_options import RequestOptions
from ..commons.errors.access_denied_error import AccessDeniedError
from ..commons.errors.error import Error
from ..commons.errors.method_not_allowed_error import MethodNotAllowedError
from ..commons.errors.not_found_error import NotFoundError
from ..commons.errors.unauthorized_error import UnauthorizedError
from ..commons.types.dataset import Dataset
from ..commons.types.dataset_run_with_items import DatasetRunWithItems
from .types.create_dataset_request import CreateDatasetRequest
from .types.delete_dataset_run_response import DeleteDatasetRunResponse
from .types.paginated_dataset_runs import PaginatedDatasetRuns
from .types.paginated_datasets import PaginatedDatasets

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class DatasetsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self,
        *,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedDatasets:
        """
        Get all datasets

        Parameters
        ----------
        page : typing.Optional[int]
            page number, starts at 1

        limit : typing.Optional[int]
            limit of items per page

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedDatasets

        Examples
        --------
        from langfuse.client import FernLangfuse

        client = FernLangfuse(
            x_langfuse_sdk_name="YOUR_X_LANGFUSE_SDK_NAME",
            x_langfuse_sdk_version="YOUR_X_LANGFUSE_SDK_VERSION",
            x_langfuse_public_key="YOUR_X_LANGFUSE_PUBLIC_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.datasets.list()
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/public/v2/datasets",
            method="GET",
            params={"page": page, "limit": limit},
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(PaginatedDatasets, _response.json())  # type: ignore
            if _response.status_code == 400:
                raise Error(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            if _response.status_code == 401:
                raise UnauthorizedError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            if _response.status_code == 403:
                raise AccessDeniedError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            if _response.status_code == 404:
                raise NotFoundError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(
        self,
        dataset_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Dataset:
        """
        Get a dataset

        Parameters
        ----------
        dataset_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dataset

        Examples
        --------
        from langfuse.client import FernLangfuse

        client = FernLangfuse(
            x_langfuse_sdk_name="YOUR_X_LANGFUSE_SDK_NAME",
            x_langfuse_sdk_version="YOUR_X_LANGFUSE_SDK_VERSION",
            x_langfuse_public_key="YOUR_X_LANGFUSE_PUBLIC_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.datasets.get(
            dataset_name="datasetName",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/public/v2/datasets/{jsonable_encoder(dataset_name)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(Dataset, _response.json())  # type: ignore
            if _response.status_code == 400:
                raise Error(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            if _response.status_code == 401:
                raise UnauthorizedError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            if _response.status_code == 403:
                raise AccessDeniedError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            if _response.status_code == 404:
                raise NotFoundError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create(
        self,
        *,
        request: CreateDatasetRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Dataset:
        """
        Create a dataset

        Parameters
        ----------
        request : CreateDatasetRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dataset

        Examples
        --------
        from langfuse import CreateDatasetRequest
        from langfuse.client import FernLangfuse

        client = FernLangfuse(
            x_langfuse_sdk_name="YOUR_X_LANGFUSE_SDK_NAME",
            x_langfuse_sdk_version="YOUR_X_LANGFUSE_SDK_VERSION",
            x_langfuse_public_key="YOUR_X_LANGFUSE_PUBLIC_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.datasets.create(
            request=CreateDatasetRequest(
                name="name",
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/public/v2/datasets",
            method="POST",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(Dataset, _response.json())  # type: ignore
            if _response.status_code == 400:
                raise Error(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            if _response.status_code == 401:
                raise UnauthorizedError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            if _response.status_code == 403:
                raise AccessDeniedError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            if _response.status_code == 404:
                raise NotFoundError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_run(
        self,
        dataset_name: str,
        run_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DatasetRunWithItems:
        """
        Get a dataset run and its items

        Parameters
        ----------
        dataset_name : str

        run_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DatasetRunWithItems

        Examples
        --------
        from langfuse.client import FernLangfuse

        client = FernLangfuse(
            x_langfuse_sdk_name="YOUR_X_LANGFUSE_SDK_NAME",
            x_langfuse_sdk_version="YOUR_X_LANGFUSE_SDK_VERSION",
            x_langfuse_public_key="YOUR_X_LANGFUSE_PUBLIC_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.datasets.get_run(
            dataset_name="datasetName",
            run_name="runName",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/public/datasets/{jsonable_encoder(dataset_name)}/runs/{jsonable_encoder(run_name)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(DatasetRunWithItems, _response.json())  # type: ignore
            if _response.status_code == 400:
                raise Error(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            if _response.status_code == 401:
                raise UnauthorizedError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            if _response.status_code == 403:
                raise AccessDeniedError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            if _response.status_code == 404:
                raise NotFoundError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete_run(
        self,
        dataset_name: str,
        run_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DeleteDatasetRunResponse:
        """
        Delete a dataset run and all its run items. This action is irreversible.

        Parameters
        ----------
        dataset_name : str

        run_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteDatasetRunResponse

        Examples
        --------
        from langfuse.client import FernLangfuse

        client = FernLangfuse(
            x_langfuse_sdk_name="YOUR_X_LANGFUSE_SDK_NAME",
            x_langfuse_sdk_version="YOUR_X_LANGFUSE_SDK_VERSION",
            x_langfuse_public_key="YOUR_X_LANGFUSE_PUBLIC_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.datasets.delete_run(
            dataset_name="datasetName",
            run_name="runName",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/public/datasets/{jsonable_encoder(dataset_name)}/runs/{jsonable_encoder(run_name)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(
                    DeleteDatasetRunResponse, _response.json()
                )  # type: ignore
            if _response.status_code == 400:
                raise Error(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            if _response.status_code == 401:
                raise UnauthorizedError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            if _response.status_code == 403:
                raise AccessDeniedError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            if _response.status_code == 404:
                raise NotFoundError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_runs(
        self,
        dataset_name: str,
        *,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedDatasetRuns:
        """
        Get dataset runs

        Parameters
        ----------
        dataset_name : str

        page : typing.Optional[int]
            page number, starts at 1

        limit : typing.Optional[int]
            limit of items per page

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedDatasetRuns

        Examples
        --------
        from langfuse.client import FernLangfuse

        client = FernLangfuse(
            x_langfuse_sdk_name="YOUR_X_LANGFUSE_SDK_NAME",
            x_langfuse_sdk_version="YOUR_X_LANGFUSE_SDK_VERSION",
            x_langfuse_public_key="YOUR_X_LANGFUSE_PUBLIC_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.datasets.get_runs(
            dataset_name="datasetName",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/public/datasets/{jsonable_encoder(dataset_name)}/runs",
            method="GET",
            params={"page": page, "limit": limit},
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(PaginatedDatasetRuns, _response.json())  # type: ignore
            if _response.status_code == 400:
                raise Error(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            if _response.status_code == 401:
                raise UnauthorizedError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            if _response.status_code == 403:
                raise AccessDeniedError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            if _response.status_code == 404:
                raise NotFoundError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncDatasetsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self,
        *,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedDatasets:
        """
        Get all datasets

        Parameters
        ----------
        page : typing.Optional[int]
            page number, starts at 1

        limit : typing.Optional[int]
            limit of items per page

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedDatasets

        Examples
        --------
        import asyncio

        from langfuse.client import AsyncFernLangfuse

        client = AsyncFernLangfuse(
            x_langfuse_sdk_name="YOUR_X_LANGFUSE_SDK_NAME",
            x_langfuse_sdk_version="YOUR_X_LANGFUSE_SDK_VERSION",
            x_langfuse_public_key="YOUR_X_LANGFUSE_PUBLIC_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.datasets.list()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/public/v2/datasets",
            method="GET",
            params={"page": page, "limit": limit},
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(PaginatedDatasets, _response.json())  # type: ignore
            if _response.status_code == 400:
                raise Error(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            if _response.status_code == 401:
                raise UnauthorizedError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            if _response.status_code == 403:
                raise AccessDeniedError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            if _response.status_code == 404:
                raise NotFoundError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(
        self,
        dataset_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Dataset:
        """
        Get a dataset

        Parameters
        ----------
        dataset_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dataset

        Examples
        --------
        import asyncio

        from langfuse.client import AsyncFernLangfuse

        client = AsyncFernLangfuse(
            x_langfuse_sdk_name="YOUR_X_LANGFUSE_SDK_NAME",
            x_langfuse_sdk_version="YOUR_X_LANGFUSE_SDK_VERSION",
            x_langfuse_public_key="YOUR_X_LANGFUSE_PUBLIC_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.datasets.get(
                dataset_name="datasetName",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/public/v2/datasets/{jsonable_encoder(dataset_name)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(Dataset, _response.json())  # type: ignore
            if _response.status_code == 400:
                raise Error(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            if _response.status_code == 401:
                raise UnauthorizedError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            if _response.status_code == 403:
                raise AccessDeniedError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            if _response.status_code == 404:
                raise NotFoundError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create(
        self,
        *,
        request: CreateDatasetRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Dataset:
        """
        Create a dataset

        Parameters
        ----------
        request : CreateDatasetRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dataset

        Examples
        --------
        import asyncio

        from langfuse import CreateDatasetRequest
        from langfuse.client import AsyncFernLangfuse

        client = AsyncFernLangfuse(
            x_langfuse_sdk_name="YOUR_X_LANGFUSE_SDK_NAME",
            x_langfuse_sdk_version="YOUR_X_LANGFUSE_SDK_VERSION",
            x_langfuse_public_key="YOUR_X_LANGFUSE_PUBLIC_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.datasets.create(
                request=CreateDatasetRequest(
                    name="name",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/public/v2/datasets",
            method="POST",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(Dataset, _response.json())  # type: ignore
            if _response.status_code == 400:
                raise Error(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            if _response.status_code == 401:
                raise UnauthorizedError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            if _response.status_code == 403:
                raise AccessDeniedError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            if _response.status_code == 404:
                raise NotFoundError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_run(
        self,
        dataset_name: str,
        run_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DatasetRunWithItems:
        """
        Get a dataset run and its items

        Parameters
        ----------
        dataset_name : str

        run_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DatasetRunWithItems

        Examples
        --------
        import asyncio

        from langfuse.client import AsyncFernLangfuse

        client = AsyncFernLangfuse(
            x_langfuse_sdk_name="YOUR_X_LANGFUSE_SDK_NAME",
            x_langfuse_sdk_version="YOUR_X_LANGFUSE_SDK_VERSION",
            x_langfuse_public_key="YOUR_X_LANGFUSE_PUBLIC_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.datasets.get_run(
                dataset_name="datasetName",
                run_name="runName",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/public/datasets/{jsonable_encoder(dataset_name)}/runs/{jsonable_encoder(run_name)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(DatasetRunWithItems, _response.json())  # type: ignore
            if _response.status_code == 400:
                raise Error(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            if _response.status_code == 401:
                raise UnauthorizedError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            if _response.status_code == 403:
                raise AccessDeniedError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            if _response.status_code == 404:
                raise NotFoundError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete_run(
        self,
        dataset_name: str,
        run_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DeleteDatasetRunResponse:
        """
        Delete a dataset run and all its run items. This action is irreversible.

        Parameters
        ----------
        dataset_name : str

        run_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteDatasetRunResponse

        Examples
        --------
        import asyncio

        from langfuse.client import AsyncFernLangfuse

        client = AsyncFernLangfuse(
            x_langfuse_sdk_name="YOUR_X_LANGFUSE_SDK_NAME",
            x_langfuse_sdk_version="YOUR_X_LANGFUSE_SDK_VERSION",
            x_langfuse_public_key="YOUR_X_LANGFUSE_PUBLIC_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.datasets.delete_run(
                dataset_name="datasetName",
                run_name="runName",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/public/datasets/{jsonable_encoder(dataset_name)}/runs/{jsonable_encoder(run_name)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(
                    DeleteDatasetRunResponse, _response.json()
                )  # type: ignore
            if _response.status_code == 400:
                raise Error(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            if _response.status_code == 401:
                raise UnauthorizedError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            if _response.status_code == 403:
                raise AccessDeniedError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            if _response.status_code == 404:
                raise NotFoundError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_runs(
        self,
        dataset_name: str,
        *,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedDatasetRuns:
        """
        Get dataset runs

        Parameters
        ----------
        dataset_name : str

        page : typing.Optional[int]
            page number, starts at 1

        limit : typing.Optional[int]
            limit of items per page

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedDatasetRuns

        Examples
        --------
        import asyncio

        from langfuse.client import AsyncFernLangfuse

        client = AsyncFernLangfuse(
            x_langfuse_sdk_name="YOUR_X_LANGFUSE_SDK_NAME",
            x_langfuse_sdk_version="YOUR_X_LANGFUSE_SDK_VERSION",
            x_langfuse_public_key="YOUR_X_LANGFUSE_PUBLIC_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.datasets.get_runs(
                dataset_name="datasetName",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/public/datasets/{jsonable_encoder(dataset_name)}/runs",
            method="GET",
            params={"page": page, "limit": limit},
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(PaginatedDatasetRuns, _response.json())  # type: ignore
            if _response.status_code == 400:
                raise Error(pydantic_v1.parse_obj_as(typing.Any, _response.json()))  # type: ignore
            if _response.status_code == 401:
                raise UnauthorizedError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            if _response.status_code == 403:
                raise AccessDeniedError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            if _response.status_code == 404:
                raise NotFoundError(
                    pydantic_v1.parse_obj_as(typing.Any, _response.json())
                )  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
