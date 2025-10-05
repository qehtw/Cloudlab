from .Comments_controller import CommentsController
from .user_controller import UsersController
from .manufacturer_controller import ManufacturersController
from .technician_controller import TechniciansController
from .user_equipment_controller import UserEquipmentController
from .repair_controller import RepairsController
from .spare_part_controller import SparePartsController
from .replaced_part_controller import ReplacedPartsController
from .repair_type_controller import RepairTypesController
from .technician_repairs_controller import TechnicianRepairsController
from .equipment_controller import EquipmentController

commentsController = CommentsController()
usersController = UsersController()
manufacturersController = ManufacturersController()
techniciansController = TechniciansController()
repair_controller = RepairsController()
spare_part_controller = SparePartsController()
replaced_part_controller = ReplacedPartsController()
repair_type_controller = RepairTypesController()
user_equipment_controller = UserEquipmentController()
technician_repairs_controller = TechnicianRepairsController()
equipment_controller = EquipmentController()

__all__ = [
    'commentsController',
    'usersController',
    'manufacturersController',
    'techniciansController',
    'repair_controller',
    'spare_part_controller',
    'replaced_part_controller',
    'repair_type_controller',
    'user_equipment_controller',
    'technician_repairs_controller'
    'equipment_controller',
]