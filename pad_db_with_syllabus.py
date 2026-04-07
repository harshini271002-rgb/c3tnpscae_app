import json

DB_FILE = "c:/Users/harsh/OneDrive/Desktop/AE/TNPSC_Quiz/questions_v2.json"

SYLLABUS_ORDER = {
    "Building Materials & Construction Practices": [
        "Brick", "Stones", "Aggregates & M-Sand", "Cement", "Admixtures",
        "Concrete (Self-compacting concrete)", "Mix Design", "Timber",
        "Recycled and modern materials - glass, plastic FRP, ceramic, steel",
        "Construction Practices: Masonry", "Construction Equipments", "Building bye-laws",
        "Provisions for fire safety, lighting and ventilation", "Acoustics"
    ],
    "Engineering Survey": [
        "Basics of Surveying", "Chain Surveying", "Compass Surveying", "Plane Table Surveying",
        "Levelling", "Computation of area and volume: L.S. and C.S.", "Contouring",
        "Theodolite surveying", "Traversing", "Tacheometry", "Triangulation", "Modern Surveying Techniques"
    ],
    "Engineering Mechanics & Strength of Materials": [
        "Forces: Types & Laws", "CoG & MI", "Friction", "Stresses and Strains",
        "Beams: SFD & BMD", "Theory of simple bending", "Deflection of beams", "Torsion",
        "Combined stresses", "Stress Transformations & Failure Theories", "Analysis of plane trusses"
    ],
    "Structural Analysis": [
        "Introduction to Analysis of Structures", "Force/Flexibility Methods of Analysis",
        "Displacement/Stiffness Methods of Analysis", "Arches", "Suspension cables",
        "Theory of columns", "Moving Loads and Influence Lines", "Matrix method",
        "Plastic theory", "Seismic analysis of high rise building"
    ],
    "Geotechnical Engineering": [
        "Formation & Types of soils", "Physical properties and testing of soils",
        "Classification of Soils for Engineering Practice", "Permeability of Soil",
        "Stress distribution in Soil", "Theory of Consolidation", "Shear strength of Soil",
        "Stability analysis of slope", "Shallow foundations", "Pile foundation",
        "Soil exploration & Sampling techniques", "Compaction of Soil", "Stabilization of soil",
        "Ground Improvement techniques"
    ],
    "Environmental Engineering": [
        "Sources & Demand of water", "Hydraulics for conveyance and transmission",
        "Characteristics, analysis of water & water borne diseases", "Functional design of water treatment",
        "Desalination plant", "Water distribution system & Pipe network analysis",
        "Planning and design of sewerage system & storm water drain",
        "Sewer appurtenances - Pumping & plumbing system in high rise building",
        "Characteristics and composition of sewage", "Sewage treatment and disposal",
        "Industrial waste water treatment", "Solid waste management",
        "Air and Noise pollution control", "E-Waste management"
    ],
    "RCC / Prestressed Concrete & Steel Structures": [
        "Working stress design concepts", "Limit state design concepts",
        "Design of Slabs (one way, Two way & Flat slabs)",
        "Design of Beam (singly, doubly reinforced & flanged sections)",
        "Design of Columns & Footings", "Staircase & Lintel",
        "Design of liquid storage structures (elevated and underground)",
        "Design of Retaining wall", "Pre-stressing - systems and Methods",
        "Design of Pre-Stressed Members for Flexure & Post tensioning slabs",
        "Design of Bolted and Welded connections", "Design of Tension members",
        "Design of Columns and Bases", "Design of Beams",
        "Design of Plate girder and Gantry girders", "Design of Members of Truss"
    ],
    "Hydraulics & Water Resources": [
        "Fluid Properties (Basics)", "Hydrostatic Pressure", "Kinematics of flow",
        "Fluid Dynamics (Applications of Bernoulli & Momentum equation)",
        "Flow through Pipes (Losses)", "Flow measurement in Channel", "Open Channel Flow",
        "Types of Pumps and Characteristics", "Water resources Planning and Management",
        "Runoff Estimation", "Hydrograph", "Flood Routing", "Flood Control",
        "Soil plant water relationship & Water requirements", "Irrigation Methods",
        "Design of Alluvial Canals", "Design of Head works",
        "Water logging and Land reclamation", "Cross Drainage works"
    ],
    "Urban & Transportation Engineering": [
        "Geometric Design of Highways", "Pavement Materials and Testing",
        "Design, Construction & Maintenance of Roads", "Railway Engineering",
        "Airport Engineering", "Harbour and Docks", "Urbanization and Slum",
        "Traffic Engineering"
    ],
    "Project Management & Estimating": [
        "Construction Management", "Project Management", "Estimation",
        "Tender", "Building Valuation"
    ]
}

try:
    with open(DB_FILE, "r", encoding="utf-8") as f:
        db = json.load(f)
except Exception:
    db = []

existing_subcats = set((q.get("subject"), q.get("subcategory")) for q in db)
added = 0

for subj, subcats in SYLLABUS_ORDER.items():
    for sc in subcats:
        if (subj, sc) not in existing_subcats:
            # Add a placeholder question
            db.append({
                "subject": subj,
                "subcategory": sc,
                "type": "Theory-based MCQ",
                "question": f"Sample placeholder question for {sc}.",
                "options": {"a": "True", "b": "False", "c": "Maybe", "d": "None"},
                "correct_answer": "a",
                "explanation": "This is a system-generated placeholder to prevent app crash on empty subcategories."
            })
            added += 1

with open(DB_FILE, "w", encoding="utf-8") as f:
    json.dump(db, f, indent=4)
    
print(f"Padded db with {added} placeholder questions.")
