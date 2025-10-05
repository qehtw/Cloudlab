from .Comment_service import CommentService
from .user_service import UserService
from .manufacturer_service import ManufacturerService
from .repair_service import RepairService
from .repair_type_service import RepairTypeService
from .replaced_part_service import ReplacedPartService
from .spare_part_service import SparePartService
from .technician_service import TechnicianService
from .user_equipment_service import UserEquipmentService

COMMENT_SERVICE = CommentService()
USER_SERVICE = UserService()
MANUFACTURER_SERVICE = ManufacturerService()
REPAIR_SERVICE = RepairService()
REPAIR_TYPE_SERVICE = RepairTypeService()
SPARE_PART_SERVICE = SparePartService()
TECHNICIAN_SERVICE = TechnicianService()
USER_EQUIPMENT_SERVICE = UserEquipmentService()

__all__ = [
    'COMMENT_SERVICE',
    'USER_SERVICE',
    'MANUFACTURER_SERVICE',
    'REPAIR_SERVICE',
    'REPAIR_TYPE_SERVICE',
    'SPARE_PART_SERVICE',
    'TECHNICIAN_SERVICE',
    'USER_EQUIPMENT_SERVICE',
]