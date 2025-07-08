import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Page configuration
st.set_page_config(
    page_title="Home Energy Calculator",
    page_icon="🏠",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #2E86AB;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .energy-card {
        background-color: #f0f8ff;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #2E86AB;
        margin: 1rem 0;
    }
    .result-card {
        background-color: #e8f5e8;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #28a745;
        margin: 1rem 0;
    }
    .warning-card {
        background-color: #fff3cd;
        padding: 1rem;
        border-radius: 10px;
        border-left: 5px solid #ffc107;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Header
    st.markdown('<h1 class="main-header">🏠 Home Energy Calculator</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Calculate your daily energy consumption based on your home and appliances</p>', unsafe_allow_html=True)
    
    # Create two columns for better layout
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Personal Information Section
        st.markdown("### 👤 Personal Information")
        
        name = st.text_input("Full Name", placeholder="Enter your full name")
        age = st.number_input("Age", min_value=1, max_value=120, value=25)
        
        # Location Information Section
        st.markdown("### 📍 Location Information")
        
        city = st.text_input("City", placeholder="Enter your city")
        area = st.text_input("Area Name", placeholder="Enter your area name")
        
        # Housing Information Section
        st.markdown("### 🏠 Housing Information")
        
        flat_tenament = st.selectbox(
            "Housing Type",
            ["Select...", "Flat", "Tenament"],
            index=0
        )
        
        facility = st.selectbox(
            "Home Configuration",
            ["Select...", "1BHK", "2BHK", "3BHK"],
            index=0
        )
        
        # Appliances Section
        st.markdown("### ⚡ Appliances")
        st.markdown("Select all appliances you use:")
        
        col_a, col_b, col_c = st.columns(3)
        
        with col_a:
            ac = st.checkbox("❄️ Air Conditioning")
        
        with col_b:
            fridge = st.checkbox("🧊 Refrigerator")
        
        with col_c:
            wm = st.checkbox("👕 Washing Machine")
        
        # Calculate button
        if st.button("🔋 Calculate Energy Consumption", type="primary"):
            if validate_inputs(name, city, area, flat_tenament, facility):
                calculate_energy(name, facility, ac, fridge, wm)
            else:
                st.error("Please fill in all required fields!")
    
    with col2:
        # Information sidebar
        st.markdown("### ℹ️ How it works")
        
        st.markdown("""
        <div class="energy-card">
        <h4>🏠 Base Energy Consumption</h4>
        <ul>
        <li><strong>1BHK:</strong> 2.4 kWh/day</li>
        <li><strong>2BHK:</strong> 3.6 kWh/day</li>
        <li><strong>3BHK:</strong> 4.8 kWh/day</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="energy-card">
        <h4>⚡ Appliance Consumption</h4>
        <ul>
        <li><strong>AC:</strong> +3.0 kWh/day</li>
        <li><strong>Fridge:</strong> +3.0 kWh/day</li>
        <li><strong>Washing Machine:</strong> +3.0 kWh/day</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="warning-card">
        <h4>💡 Energy Saving Tips</h4>
        <ul>
        <li>Use LED bulbs</li>
        <li>Unplug unused devices</li>
        <li>Optimize AC temperature</li>
        <li>Use natural light when possible</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

def validate_inputs(name, city, area, flat_tenament, facility):
    """Validate user inputs"""
    return (name and city and area and 
            flat_tenament != "Select..." and 
            facility != "Select...")

def calculate_energy(name, facility, ac, fridge, wm):
    """Calculate energy consumption using the original logic"""
    
    # Initialize energy calculation
    cal_energy = 0
    breakdown = []
    
    # Base energy calculation (your original logic)
    facility_lower = facility.lower()
    
    if facility_lower == "1bhk":
        base_energy = 2 * 0.4 + 2 * 0.8  # 2.4
        cal_energy += base_energy
        breakdown.append(("1BHK Base", base_energy))
    elif facility_lower == "2bhk":
        base_energy = 3 * 0.4 + 3 * 0.8  # 3.6
        cal_energy += base_energy
        breakdown.append(("2BHK Base", base_energy))
    elif facility_lower == "3bhk":
        base_energy = 4 * 0.4 + 4 * 0.8  # 4.8
        cal_energy += base_energy
        breakdown.append(("3BHK Base", base_energy))
    
    # Add appliances (your original logic)
    if ac:
        cal_energy += 3
        breakdown.append(("Air Conditioning", 3.0))
    
    if fridge:
        cal_energy += 3
        breakdown.append(("Refrigerator", 3.0))
    
    if wm:
        cal_energy += 3
        breakdown.append(("Washing Machine", 3.0))
    
    # Display results
    display_results(name, cal_energy, breakdown)

def display_results(name, total_energy, breakdown):
    """Display calculation results with visualizations"""
    
    st.markdown("---")
    st.markdown("## 📊 Energy Consumption Results")
    
    # Main result card
    st.markdown(f"""
    <div class="result-card">
    <h3>Hi {name}! 👋</h3>
    <h2>Your estimated daily energy consumption is <strong>{total_energy:.1f} kWh</strong></h2>
    <p>This is equivalent to approximately <strong>₹{total_energy * 5:.0f}</strong> per day at ₹5 per kWh</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Create visualization
    if breakdown:
        # Prepare data for charts
        categories = [item[0] for item in breakdown]
        values = [item[1] for item in breakdown]
        
        # Create two columns for charts
        chart_col1, chart_col2 = st.columns(2)
        
        with chart_col1:
            # Pie chart
            fig_pie = px.pie(
                values=values, 
                names=categories,
                title="Energy Distribution",
                color_discrete_sequence=px.colors.qualitative.Set3
            )
            fig_pie.update_layout(height=400)
            st.plotly_chart(fig_pie, use_container_width=True)
        
        with chart_col2:
            # Bar chart
            fig_bar = px.bar(
                x=categories,
                y=values,
                title="Energy Consumption by Category",
                labels={'x': 'Category', 'y': 'Energy (kWh)'},
                color=values,
                color_continuous_scale='Blues'
            )
            fig_bar.update_layout(height=400, showlegend=False)
            st.plotly_chart(fig_bar, use_container_width=True)
        
        # Detailed breakdown table
        st.markdown("### 📋 Detailed Breakdown")
        breakdown_df = pd.DataFrame(breakdown, columns=['Category', 'Energy (kWh)'])
        breakdown_df['Percentage'] = (breakdown_df['Energy (kWh)'] / total_energy * 100).round(1)
        breakdown_df['Cost (₹/day)'] = (breakdown_df['Energy (kWh)'] * 5).round(0)
        
        st.dataframe(breakdown_df, use_container_width=True)
        
        # Monthly and yearly projections
        st.markdown("### 📅 Projections")
        
        monthly_energy = total_energy * 30
        yearly_energy = total_energy * 365
        monthly_cost = monthly_energy * 5
        yearly_cost = yearly_energy * 5
        
        proj_col1, proj_col2, proj_col3, proj_col4 = st.columns(4)
        
        with proj_col1:
            st.metric("Monthly Energy", f"{monthly_energy:.1f} kWh")
        
        with proj_col2:
            st.metric("Yearly Energy", f"{yearly_energy:.1f} kWh")
        
        with proj_col3:
            st.metric("Monthly Cost", f"₹{monthly_cost:.0f}")
        
        with proj_col4:
            st.metric("Yearly Cost", f"₹{yearly_cost:.0f}")

# Sidebar with additional information
with st.sidebar:
    st.markdown("## 🔧 Settings")
    
    # Energy rate selector
    energy_rate = st.slider("Energy Rate (₹/kWh)", 3, 10, 5)
    
    st.markdown("## 📖 About")
    st.markdown("""
    This calculator uses a simplified model to estimate your daily energy consumption based on:
    
    - **Home size** (1BHK, 2BHK, 3BHK)
    - **Major appliances** (AC, Refrigerator, Washing Machine)
    
    The calculations are based on average consumption patterns and may vary based on actual usage, appliance efficiency, and local conditions.
    """)
    
    st.markdown("## 🎯 Energy Efficiency Tips")
    st.markdown("""
    - **Set AC to 24°C** for optimal efficiency
    - **Use inverter appliances** to save 20-30% energy
    - **Switch to LED lighting** throughout your home
    - **Unplug devices** when not in use
    - **Regular maintenance** of appliances improves efficiency
    """)

if __name__ == "__main__":
    main()