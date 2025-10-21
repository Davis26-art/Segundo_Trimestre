# =========================================
# VERIFICADOR DE CONTRASEÑA SEGURA
# =========================================

contraseña = input("Ingrese su contraseña: ")

# Requisitos
tiene_mayus = any(c.isupper() for c in contraseña)
tiene_minus = any(c.islower() for c in contraseña)
tiene_numero = any(c.isdigit() for c in contraseña)
longitud_ok = len(contraseña) >= 8

# Verificación
if tiene_mayus and tiene_minus and tiene_numero and longitud_ok:
    print("✅ Contraseña válida")
else:
    print("❌ Contraseña inválida. Debe tener al menos 8 caracteres, incluir mayúsculas, minúsculas y números.")
