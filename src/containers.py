import dependency_injector.containers as containers
import dependency_injector.providers as providers
import src.user.user_controller
import src.user.mongo_repository
import src.user.use_cases
import mongoengine


class Core(containers.DeclarativeContainer):
    config = providers.Configuration()


class Gateways(containers.DeclarativeContainer):
    mongo_connection = providers.Singleton(mongoengine.connect, Core.config.db)


class Repositories(containers.DeclarativeContainer):
    user_repository = providers.Singleton(src.user.mongo_repository.UserMongoRepository)


class Services(containers.DeclarativeContainer):
    user_service = providers.Factory(src.user.use_cases.UserUseCase, user_repository=Repositories.user_repository)


class Controllers(containers.DeclarativeContainer):
    user_factory = providers.FactoryAggregate(
        user_controller_post=providers.Factory(src.user.user_controller.UserControllerPost,
                                               user_use_case=Services.user_service),
        user_controller_delete=providers.Factory(src.user.user_controller.UserControllerDelete,
                                                 user_use_case=Services.user_service))
