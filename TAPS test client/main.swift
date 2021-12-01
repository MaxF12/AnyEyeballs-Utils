//
//  main.swift
//  AnyEyeballs
//
//  Created by Max Franke on 25.11.21.
//

import Foundation
import Network

// Initiate necessary variables and use Network.framework to create a connection to www.anyeyeballs.de
func make_connection() {
    let Url = URL.init(string: "http://www.anyeyeballs.de");
    let Endpoint = NWEndpoint.url(Url!);
    let Parameters = NWParameters.tcp;
    let Connection = NWConnection(to: Endpoint, using: Parameters);
    let Queue = DispatchQueue.init(label: "TCP")
    Connection.start(queue: Queue)
}

// Create a new connection once a second
for _ in 0...100 {
    make_connection()
    sleep(1)
}

// Keep the threat alive
while true {
    sleep(1)
}
