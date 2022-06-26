def vericarnumeropestañas (driver):
    pestanas= driver.window_handles
    if len(pestanas)==1:
        return False
    elif len(pestanas)==2:
        
        return True

def windows_visual_studio_code(driver):
    driver.switch_to.window(driver.window_handles[1])
    return True

    