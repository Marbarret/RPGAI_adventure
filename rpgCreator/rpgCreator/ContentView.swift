//
//  ContentView.swift
//  rpgCreator
//
//  Created by Marcylene Barreto on 12/07/23.
//

import SwiftUI

struct ContentView: View {
    @State private var showSheet = false
    
    var body: some View {
        ZStack(alignment: .top) {
            Image("twice-1")
                .resizable()
                .scaledToFill()
                .clipped()
                .ignoresSafeArea()
            
            Button("Show Bottom Sheet") {
                showSheet.toggle()
            }
            .tint(.black)
            .buttonStyle(.borderedProminent)
            .sheet(isPresented: $showSheet) {
                Text("This is the expandable bottom sheet.")
                    .presentationDetents([ .medium, .large])
            }
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}

//struct BasicBottomSheet: View {
//    @State private var showSheet = false
//
//    var body: some View {
//        VStack {
//            Button("Show Bottom Sheet") {
//                showSheet.toggle()
//            }
//            .buttonStyle(.borderedProminent)
//            .sheet(isPresented: $showSheet) {
//                Text("This is the expandable bottom sheet.")
//                    .presentationDetents([.medium, .large])
//            }
//
//            Spacer()
//        }
//    }
//}
