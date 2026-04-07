import json
import os

DB_FILE = r"c:\Users\harsh\OneDrive\Desktop\AE\TNPSC_Quiz\questions_v2.json"

SYLLABUS_ORDER = {
    "Building Materials & Construction Practices": ["Characteristics, Properties and Uses of Building Materials", "Brick", "Stones", "Aggregates & M-Sand", "Lime, Mortar & Concrete", "Timber, Metals & Plastics", "Concrete (Self-compacting concrete)", "Mix Design", "Admixtures", "Construction Practices: Masonry", "Masonry & Scaffolding", "Roofing & Arches", "Damp-proofing & Flooring", "Construction Equipments", "Building bye-laws", "Doors, Windows & Stairs", "Acoustics", "Foundations & Excavation", "Provisions for fire safety, lighting and ventilation", "Recycled and modern materials - glass, plastic FRP, ceramic, steel"],
    "Engineering Survey": ["Chain Surveying", "Compass Surveying", "Plane Table Surveying", "Levelling", "Theodolite Surveying", "Tacheometry", "Triangulation", "Curve Surveying", "Modern Surveying Methods (Total Station, GPS)", "Photogrammetry", "Remote Sensing", "GIS"],
    "Engineering Mechanics & Strength of Materials": ["Statics of Particles", "Equilibrium of Rigid Bodies", "Friction", "Center of Gravity & Moment of Inertia", "Simple Stress & Strain", "Shear Force & Bending Moment Diagram", "Stresses in Beams", "Torsion of Circular Shafts", "Deflection of Beams", "Thin Cylindrical & Spherical Shells"],
    "Structural Analysis": ["Analysis of Indeterminate Structures", "Slope Deflection Method", "Moment Distribution Method", "Matrix Analysis", "Arches", "Suspension Bridges", "Influence Lines", "Plastic Analysis"],
    "Geotechnical Engineering": ["Soil Properties", "Soil Classification", "Permeability & Seepage", "Effective Stress Principle", "Consolidation", "Shear Strength", "Compaction", "Bearing Capacity of Soils", "Shallow Foundations", "Deep Foundations"],
    "Environmental Engineering": ["Sources & Demand of water", "Hydraulics for conveyance and transmission", "Characteristics, analysis of water & water borne diseases", "Functional design of water treatment", "Desalination plant", "Water distribution system & Pipe network analysis", "Planning and design of sewerage system & storm water drain", "Sewer appurtenances - Pumping & plumbing system in high rise building", "Characteristics and composition of sewage", "Sewage treatment and disposal", "Industrial waste water treatment", "Solid waste management", "Air and Noise pollution control", "E-Waste management"],
    "RCC / Prestressed Concrete & Steel Structures": ["Working stress design concepts", "Limit state design concepts", "Design of Slabs (one way, Two way & Flat slabs)", "Design of Beam (singly, doubly reinforced & flanged sections)", "Design of Columns & Footings", "Staircase & Lintel", "Design of liquid storage structures (elevated and underground)", "Design of Retaining wall", "Pre-stressing - systems and Methods", "Design of Pre-Stressed Members for Flexure & Post tensioning slabs", "Design of Bolted and Welded connections", "Design of Tension members", "Design of Columns and Bases", "Design of Beams", "Design of Plate girder and Gantry girders", "Design of Members of Truss"],
    "Hydraulics & Water Resources": ["Fluid Properties (Basics)", "Hydrostatic Pressure", "Kinematics of flow", "Fluid Dynamics (Applications of Bernoulli & Momentum equation)", "Flow through Pipes (Losses)", "Flow measurement in Channel", "Open Channel Flow", "Types of Pumps and Characteristics", "Water resources Planning and Management", "Runoff Estimation", "Hydrograph", "Flood Routing", "Flood Control", "Soil plant water relationship & Water requirements", "Irrigation Methods", "Design of Alluvial Canals", "Design of Head works", "Water logging and Land reclamation", "Cross Drainage works"],
    "Urban & Transportation Engineering": ["Geometric Design of Highways", "Pavement Materials and Testing", "Design, Construction & Maintenance of Roads", "Railway Engineering", "Airport Engineering", "Harbour and Docks", "Urbanization and Slum", "Traffic Engineering"],
    "Project Management & Estimating": ["Construction Management", "Project Management", "Estimation", "Tender", "Building Valuation"]
}

def check_status():
    if not os.path.exists(DB_FILE):
        print("DB File not found.")
        return
    
    with open(DB_FILE, 'r', encoding='utf-8') as f:
        db = json.load(f)
        
    print(f"Total Questions in DB: {len(db)}")
    
    for subj, topics in SYLLABUS_ORDER.items():
        print(f"\n--- Subject: {subj} ---")
        subj_qs = [q for q in db if q.get("subject") == subj]
        for topic in topics:
            # Fuzzy match same as app.py
            topic_qs = []
            for q in subj_qs:
                q_sc = q.get("subcategory", "")
                if topic.lower() in q_sc.lower() or q_sc.lower() in topic.lower():
                    topic_qs.append(q)
            
            count = len(topic_qs)
            status = "GREEN" if count >= 25 else "RED (Needs " + str(25 - count) + ")"
            print(f"  [{status}] {topic}: {count}/25")

if __name__ == "__main__":
    check_status()
