import gradio as gr

def pump_power(flow_rate, head, density, efficiency):
    try:
        g = 9.81  # gravity (m/s²)
        efficiency = efficiency / 100  # convert % to decimal

        # Convert flow rate from L/s to m³/s
        flow_rate_m3s = flow_rate / 1000  

        # Hydraulic power formula
        power = (density * g * flow_rate_m3s * head) / efficiency  
        return f"{power:.2f} Watts"
    except Exception as e:
        return f"Error: {str(e)}"

# Gradio UI
with gr.Blocks() as demo:
    gr.Markdown("# ⚙️ Power Pump Calculator\nEnter the parameters to calculate Pump Power.")
    
    with gr.Row():
        flow_rate = gr.Number(label="Flow Rate (L/s)", value=10)
        head = gr.Number(label="Head (m)", value=20)
    
    with gr.Row():
        density = gr.Number(label="Fluid Density (kg/m³)", value=1000)
        efficiency = gr.Number(label="Pump Efficiency (%)", value=85)
    
    output = gr.Textbox(label="Pump Power (Watts)")
    
    calc_btn = gr.Button("Calculate Power")
    calc_btn.click(fn=pump_power, inputs=[flow_rate, head, density, efficiency], outputs=output)

demo.launch()
