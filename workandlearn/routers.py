from appwnl.api.viewsets import *
from rest_framework_nested import routers

router = routers.SimpleRouter()

router.register('empresa', EmpresaViewSet, base_name='empresa')
router.register('desenvolvedor',
                DesenvolvedorViewSet,
                base_name='desenvolvedor')

empresa_router = routers.NestedSimpleRouter(router,
                                            'empresa',
                                            lookup='empresa')

empresa_router.register('tecnologia',
                        TecnologiaEmpresaViewSet,
                        base_name='tecnologia')
empresa_router.register('local', LocalViewSet, base_name='local')
empresa_router.register('reserva', ReservaEmpresaViewSet, base_name='reserva')

dev_router = routers.NestedSimpleRouter(router,
                                        'desenvolvedor',
                                        lookup='desenvolvedor')

dev_router.register('endereco', EnderecoViewSet, base_name='endereco')
dev_router.register('tecnologia',
                    TecnologiaDesenvolvedorViewSet,
                    base_name='tecnologia')
dev_router.register('reserva',
                    ReservaDesenvolvedorViewSet,
                    base_name='reserva')

#local_router = routers.NestedSimpleRouter(empresa_router,
#                                          'endereco',
#                                          lookup='endereco')
#
#local_router.register('local', LocalViewSet, base_name='local')
"""
for url in router.urls:
    print(url)
"""