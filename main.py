from agent import create_agent

def main():
    print("🤖 Bienvenido a BlackTechSec CLI Agent.")
    print("Escribe tu pregunta o comando (o 'salir' para terminar):")

    agent = create_agent()

    while True:
        entrada = input("> ")
        if entrada.lower() in ['salir', 'exit', 'quit']:
            print("👋 Hasta luego.")
            break
        try:
            respuesta = agent.invoke({"input": entrada}).content
            print(f"\n💬 {respuesta}\n")
        except Exception as e:
            print(f"\n❌ Error procesando tu solicitud: {e}\n")

if __name__ == "__main__":
    main()
