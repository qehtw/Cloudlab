from flask import Flask
from .error_handler import err_handler_bp


def register_routes(app: Flask) -> None:
    app.register_blueprint(err_handler_bp)
    from .user_route import user_bp
    from .repair_route import repair_bp
    from .equipment_route import equipment_bp
    from .manufacturer_route import manufacturer_bp
    from .repair_type_route import repair_type_bp
    from .replaced_part_route import replaced_part_bp
    from .spare_parts_route import spare_part_bp
    from .technician_repairs_route import technician_repairs_bp
    from .technician_route import technician_bp
    from .technician_schedule_route import technician_schedule_bp
    from .comment_route import comment_bp
    from .user_equipment_route import user_equipment_bp

    app.register_blueprint(user_bp)
    app.register_blueprint(repair_bp)
    app.register_blueprint(manufacturer_bp)
    app.register_blueprint(repair_type_bp)
    app.register_blueprint(spare_part_bp)
    app.register_blueprint(technician_repairs_bp)
    app.register_blueprint(technician_schedule_bp)
    app.register_blueprint(replaced_part_bp)
    app.register_blueprint(equipment_bp)
    app.register_blueprint(technician_bp)
    app.register_blueprint(comment_bp)
    app.register_blueprint(user_equipment_bp)
